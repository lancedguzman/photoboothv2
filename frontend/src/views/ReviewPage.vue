<template>
  <div class="review-page">
    <img src="http://localhost:8000/media/assets/cloud-3.svg" class="cloud cloud-bg" alt="cloud" />

    <div class="content-wrapper">
      <h1 class="header-text">Review Your Photos</h1>

      <div class="photos-grid">
        <div v-for="index in 4" :key="index" class="photo-preview">
          <!-- Display image if it exists in the store -->
          <img v-if="photoStore.photos[index - 1]" :src="photoStore.photos[index - 1]" class="preview-img" />
          <p v-else>No Photo</p>
        </div>
      </div>

      <div class="actions">
        <button class="btn secondary" @click="retakeAll">Retake All</button>
        <button class="btn primary" @click="submitToBackend" :disabled="isSubmitting">
          {{ isSubmitting ? 'Generating...' : 'Print & Generate' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { usePhotoStore } from '../stores/photoStore'

const router = useRouter()
const photoStore = usePhotoStore()
const isSubmitting = ref(false)

const retakeAll = () => {
  photoStore.clearPhotos()
  router.push('/capture')
}

// Converts base64 to a Blob for uploading
const urlToBlob = async (url) => {
  const response = await fetch(url)
  return await response.blob()
}

const submitToBackend = async () => {
  isSubmitting.value = true

  const formData = new FormData()

  try {
    // Convert base64 store images to Blob files and append to form
    for (let i = 0; i < 4; i++) {
      if (photoStore.photos[i]) {
        const blob = await urlToBlob(photoStore.photos[i])
        formData.append(`photo_${i + 1}`, blob, `photo_${i + 1}.jpg`)
      }
    }

    // POST to the Django backend
    const response = await fetch('http://localhost:8000/api/sessions/create/', {
      method: 'POST',
      body: formData
    })

    if (!response.ok) throw new Error('Failed to upload photos')

    const data = await response.json()

    // Push to Result page, passing the generated session UUID in the URL
    router.push(`/result?id=${data.id}`)

  } catch (error) {
    console.error("Error submitting to backend:", error)
    alert("There was an error generating your photos. Please try again.")
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.review-page {
  position: relative;
  min-height: 100vh;
  background-color: #5B8FFF;
  text-align: center;
  padding: 20px;
  color: white;
  overflow: hidden;
}
.cloud-bg {
  position: absolute;
  bottom: 10%;
  right: 5%;
  width: 250px;
  opacity: 0.6;
  z-index: 1;
}
.content-wrapper {
  position: relative;
  z-index: 10;
}
.header-text {
  color: #FFD700;
  margin-bottom: 30px;
}
.photos-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  max-width: 600px;
  margin: 0 auto 40px auto;
}
.photo-preview {
  background: white;
  aspect-ratio: 4 / 3;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
}
.preview-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.btn {
  padding: 15px 30px;
  margin: 0 10px;
  font-size: 18px;
  border-radius: 30px;
  cursor: pointer;
  border: none;
  font-weight: bold;
  transition: transform 0.2s;
}
.btn:hover:not(:disabled) {
  transform: scale(1.05);
}
.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
.secondary {
  background: white;
  color: #EA4335;
}
.primary {
  background: #34A853;
  color: white;
}
</style>
