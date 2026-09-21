<template>
  <div class="capture-page">
    <!-- Top Left GDG Logo -->
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/gdg-logo.svg" class="decor gdg-logo" alt="GDG Logo" />

    <!-- Background Clouds -->
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-tl" alt="cloud" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-tr" alt="cloud" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-ml" alt="cloud" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-mr" alt="cloud" />

    <div class="main-layout">
      <!-- Main camera view -->
      <div class="camera-feed">
        <video ref="videoElement" autoplay playsinline class="video-stream" :class="{ flash: isFlashing }"></video>

        <!-- Dynamic Cloud SVG Countdown -->
        <img
          v-if="isCountingDown && countdownNumber > 0 && !isSubmitting"
          :src="`https://gdgloyola.pythonanywhere.com/media/assets/cloud-${countdownNumber}.svg`"
          class="countdown-image"
          alt="countdown"
        />

        <!-- Loading state overlay during upload -->
        <h2 v-if="isSubmitting" class="camera-status processing-text">Processing your photos...</h2>

        <h2 v-if="!isCameraActive && !isSubmitting" class="camera-status">{{ cameraStatusText }}</h2>
      </div>

      <!-- Sidebar for thumbnails reading from Pinia store -->
      <div class="thumbnail-sidebar">
        <div v-for="index in 4" :key="index" class="thumbnail-slot">
          <img v-if="photoStore.photos[index - 1]" :src="photoStore.photos[index - 1]" class="thumbnail-img" />
          <button v-if="photoStore.photos[index - 1]" class="refresh-icon" @click="retakeSingle(index - 1)">↻</button>
        </div>
      </div>
    </div>

    <!-- Bottom Left Decorations -->
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/blue-box.svg" class="decor blue-box" alt="blue box" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/googley-laptop.svg" class="decor laptop-robot" alt="laptop robot" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/yellow-box.svg" class="decor yellow-box-robot" alt="yellow box robot" />

    <!-- Bottom Right Decoration -->
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/blimp.svg" class="decor blimp" alt="blimp" />

    <!-- Floating Capture Button & Finish Button -->
    <div class="controls">
      <button class="capture-btn" @click="startSequence" :disabled="isSequenceActive">
        <img src="https://gdgloyola.pythonanywhere.com/media/assets/capture-button.svg" alt="Capture" class="capture-img" />
      </button>

      <!-- Updated Finish Button using SVG and awaiting user input -->
      <button
        v-if="!isSequenceActive && photoStore.photos.some(p => p)"
        class="finish-btn"
        @click="finishSession"
        :disabled="isSubmitting"
      >
        <img src="https://gdgloyola.pythonanywhere.com/media/assets/finish-button.svg" alt="Finish" class="finish-img" />
      </button>
    </div>

    <canvas ref="canvasElement" style="display: none;"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { usePhotoStore } from '../stores/photoStore'

const router = useRouter()
const photoStore = usePhotoStore()

// Refs
const videoElement = ref(null)
const canvasElement = ref(null)
const isCameraActive = ref(false)
const cameraStatusText = ref('live view from camera')
let mediaStream = null

// Sequence State
const isSequenceActive = ref(false)
const isCountingDown = ref(false)
const countdownNumber = ref(3)
const isFlashing = ref(false)
const isSubmitting = ref(false)
const currentShotIndex = ref(0)

const startCamera = async () => {
  try {
    mediaStream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: 'user', width: { ideal: 1280 }, height: { ideal: 960 } }
    })
    if (videoElement.value) {
      videoElement.value.srcObject = mediaStream
      isCameraActive.value = true
    }
  } catch (error) {
    console.error('Error accessing the camera:', error)
    cameraStatusText.value = 'Camera access denied or not available.'
  }
}

const stopCamera = () => {
  if (mediaStream) {
    mediaStream.getTracks().forEach(track => track.stop())
  }
}

onMounted(() => {
  startCamera()
})

onBeforeUnmount(() => {
  stopCamera()
})

// --- Capture Logic ---
const startSequence = async () => {
  if (isSequenceActive.value) return
  isSequenceActive.value = true
  currentShotIndex.value = 0
  photoStore.clearPhotos()

  for (let i = 0; i < 4; i++) {
    // Break the automated loop if the user interrupts it to retake a photo
    if (!isSequenceActive.value) return

    currentShotIndex.value = i
    await runCountdown(3)

    // Check again in case it was interrupted during the 3-second countdown
    if (!isSequenceActive.value) return

    takePicture(i)
  }

  // End the sequence without automatically submitting to ResultPage
  if (isSequenceActive.value) {
    isSequenceActive.value = false
  }
}

const runCountdown = (seconds) => {
  return new Promise((resolve) => {
    isCountingDown.value = true
    countdownNumber.value = seconds

    const interval = setInterval(() => {
      countdownNumber.value -= 1
      if (countdownNumber.value <= 0) {
        clearInterval(interval)
        isCountingDown.value = false
        resolve()
      }
    }, 1000)
  })
}

const takePicture = (index) => {
  const video = videoElement.value
  const canvas = canvasElement.value
  const context = canvas.getContext('2d')

  canvas.width = video.videoWidth
  canvas.height = video.videoHeight
  context.translate(canvas.width, 0)
  context.scale(-1, 1)
  context.drawImage(video, 0, 0, canvas.width, canvas.height)

  isFlashing.value = true
  setTimeout(() => isFlashing.value = false, 150)

  const imageData = canvas.toDataURL('image/jpeg')
  photoStore.setPhoto(index, imageData)
}

const retakeSingle = async (index) => {
  if (isSequenceActive.value) {
     isSequenceActive.value = false
  }
  await runCountdown(3)
  takePicture(index)
}

// Converts base64 to a Blob for uploading
const urlToBlob = async (url) => {
  const response = await fetch(url)
  return await response.blob()
}

const finishSession = async () => {
  isSubmitting.value = true
  const formData = new FormData()

  try {
    for (let i = 0; i < 4; i++) {
      if (photoStore.photos[i]) {
        const blob = await urlToBlob(photoStore.photos[i])
        formData.append(`photo_${i + 1}`, blob, `photo_${i + 1}.jpg`)
      }
    }

    const response = await fetch('https://gdgloyola.pythonanywhere.com/api/sessions/create/', {
      method: 'POST',
      body: formData
    })

    if (!response.ok) throw new Error('Failed to upload photos')

    const data = await response.json()
    router.push(`/result?id=${data.id}`)

  } catch (error) {
    console.error("Error submitting to backend:", error)
    alert("There was an error generating your photos. Please try again.")
    isSequenceActive.value = false
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.capture-page {
  position: relative;
  height: 100vh;
  background-color: #5B8FFF;
  display: flex;
  flex-direction: column;
  padding: 40px;
  overflow: hidden;
}

/* Background Clouds */
.cloud {
  position: absolute;
  opacity: 0.9;
  z-index: 1;
}
.cloud-tl { top: -20px; left: 10%; width: 250px; }
.cloud-tr { top: 0; right: 25%; width: 180px; }
.cloud-ml { top: 30%; left: -50px; width: 200px; }
.cloud-mr { top: 40%; right: -20px; width: 220px; }

/* Absolute Decorative Assets */
.decor {
  position: absolute;
  z-index: 15;
}
.gdg-logo { top: 20px; left: 20px; width: 80px; }
.blue-box { bottom: -10px; left: -10px; width: 180px; }
.laptop-robot { bottom: 80px; left: 20px; width: 150px; mix-blend-mode: screen; }
.yellow-box-robot { bottom: 10px; left: 180px; width: 160px; mix-blend-mode: screen; }
.blimp { bottom: 20px; right: 20px; width: 160px; }

/* Layout adjustments */
.main-layout {
  display: flex;
  flex: 1;
  gap: 30px;
  justify-content: center;
  align-items: center;
  z-index: 10;
  padding-bottom: 60px;
}

/* Wider Camera Feed Shape */
.camera-feed {
  flex: 0.75;
  aspect-ratio: 16 / 10;
  max-height: 70vh;
  background: white;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.15);
}
.video-stream {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scaleX(-1);
  transition: filter 0.1s;
}

.flash { filter: brightness(2) contrast(1.5); }

.countdown-image {
  position: absolute;
  width: 250px;
  z-index: 5;
  filter: drop-shadow(0px 4px 15px rgba(0,0,0,0.5));
}

.camera-status {
  position: absolute;
  color: black;
  font-family: 'Google Sans Code', monospace;
  font-size: 2rem;
  font-weight: bold;
  z-index: 2;
}

.processing-text { background: rgba(255, 255, 255, 0.85); padding: 10px 30px; border-radius: 30px; z-index: 6; }

/* Sidebar Styling */
.thumbnail-sidebar {
  flex: 0.2;
  display: flex;
  flex-direction: column;
  gap: 15px;
  height: 100%;
  max-height: 70vh;
}
.thumbnail-slot {
  flex: 1;
  background: white;
  border-radius: 15px;
  position: relative;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
}
.thumbnail-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.refresh-icon {
  position: absolute;
  top: 5px;
  right: 5px;
  color: red;
  background: rgba(255,255,255,0.7);
  border: none;
  border-radius: 50%;
  width: 25px;
  height: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  font-size: 1rem;
}

/* Floating Controls */
.controls {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 25;
  display: flex;
  align-items: center;
  gap: 20px;
}
.capture-btn {
  background: none;
  border: none;
  cursor: pointer;
  transition: transform 0.2s;
  padding: 0;
}
.capture-img {
  width: 220px;
}
.capture-btn:hover:not(:disabled) {
  transform: scale(1.05);
}
.capture-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.finish-btn {
  background: none;
  border: none;
  cursor: pointer;
  transition: transform 0.2s;
  padding: 0;
}
.finish-img {
  width: 200px;
}
.finish-btn:hover:not(:disabled) {
  transform: scale(1.05);
}
.finish-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
