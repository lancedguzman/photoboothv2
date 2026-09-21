<template>
  <div class="capture-page">
    <img src="http://localhost:8000/media/assets/cloud-2.svg" class="cloud cloud-top" alt="cloud" />

    <div class="main-layout">
      <!-- Main camera view -->
      <div class="camera-feed">
        <video ref="videoElement" autoplay playsinline class="video-stream" :class="{ flash: isFlashing }"></video>
        <h1 v-if="isCountingDown" class="countdown-text">{{ countdownNumber }}</h1>
        <h2 v-if="!isCameraActive" class="camera-status">{{ cameraStatusText }}</h2>
      </div>

      <!-- Sidebar for thumbnails reading from Pinia store -->
      <div class="thumbnail-sidebar">
        <div v-for="index in 4" :key="index" class="thumbnail-slot">
          <img v-if="photoStore.photos[index - 1]" :src="photoStore.photos[index - 1]" class="thumbnail-img" />
          <button v-if="photoStore.photos[index - 1]" class="refresh-icon" @click="retakeSingle(index - 1)">↻</button>
        </div>
      </div>
    </div>

    <div class="controls">
      <button class="capture-btn" @click="startSequence" :disabled="isSequenceActive">
        <img src="http://localhost:8000/media/assets/capture-button.svg" alt="Capture" />
      </button>
    </div>

    <canvas ref="canvasElement" style="display: none;"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { usePhotoStore } from '../stores/photoStore' // Import the store

const router = useRouter()
const photoStore = usePhotoStore() // Initialize store

// Refs
const videoElement = ref(null)
const canvasElement = ref(null)
const isCameraActive = ref(false)
const cameraStatusText = ref('Requesting camera access...')
let mediaStream = null

// Sequence State
const isSequenceActive = ref(false)
const isCountingDown = ref(false)
const countdownNumber = ref(5)
const isFlashing = ref(false)
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
  photoStore.clearPhotos() // Clear old photos in the store

  for (let i = 0; i < 4; i++) {
    currentShotIndex.value = i
    await runCountdown(i === 0 ? 5 : 3)
    takePicture(i)
  }

  setTimeout(() => {
    router.push('/review')
  }, 1500)
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

  // Save base64 image data directly to Pinia store
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
</script>

<style scoped>
/* Keep existing layout styles */
.capture-page {
  position: relative;
  height: 100vh;
  background-color: #5B8FFF;
  display: flex;
  flex-direction: column;
  padding: 20px;
  overflow: hidden;
}
.cloud-top {
  position: absolute;
  top: 5%;
  left: 30%;
  width: 150px;
  opacity: 0.8;
  z-index: 1;
}
.main-layout {
  display: flex;
  flex: 1;
  gap: 30px;
  justify-content: center;
  align-items: center;
  z-index: 10;
}
.camera-feed {
  flex: 0.6;
  aspect-ratio: 4 / 3;
  max-height: 65vh;
  background: black;
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

/* Flash effect */
.flash {
  filter: brightness(2) contrast(1.5);
}

/* Countdown Overlay */
.countdown-text {
  position: absolute;
  font-size: 8rem;
  color: white;
  text-shadow: 0px 4px 15px rgba(0,0,0,0.5);
  z-index: 5;
  margin: 0;
}

.camera-status {
  position: absolute;
  color: white;
  z-index: 2;
}
.thumbnail-sidebar {
  flex: 0.15;
  display: flex;
  flex-direction: column;
  gap: 15px;
  height: 100%;
  max-height: 65vh;
}
.thumbnail-slot {
  flex: 1;
  background: white;
  border-radius: 10px;
  position: relative;
  aspect-ratio: 4 / 3;
  overflow: hidden; /* Ensure thumbnail image doesn't break border radius */
}

/* Thumbnail Image Display */
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
.controls {
  text-align: center;
  margin-top: 10px;
  margin-bottom: 20px;
  z-index: 10;
}
.capture-btn {
  background: none;
  border: none;
  cursor: pointer;
  transition: transform 0.2s;
}
.capture-btn:hover:not(:disabled) {
  transform: scale(1.05);
}
.capture-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
