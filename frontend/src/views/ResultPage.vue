<template>
  <div class="result-page">
    <div class="header">
      <h1 class="title">your</h1>
      <img src="http://localhost:8000/media/assets/googley-logo.svg" alt="Googley" class="header-logo" />
      <h1 class="title">picture is ready!</h1>
    </div>

    <div v-if="isLoading" class="loading-state">
      <h2 style="color: white;">Stitching your Googley moment...</h2>
    </div>

    <div v-else class="result-layout">
      <!-- QR Code Section -->
      <div class="qr-section">
        <div class="qr-placeholder">
          <img v-if="sessionData?.qr_code" :src="sessionData.qr_code" alt="QR Code" class="final-img" />
        </div>
        <p class="qr-text">get a digital copy</p>
      </div>

      <!-- Final Composite Frame from Backend -->
      <div class="composite-frame">
         <img v-if="sessionData?.composite_frame" :src="sessionData.composite_frame" alt="Composite Photo" class="final-img" />
      </div>
    </div>

    <button class="btn home-btn" @click="goHome">Finish</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const sessionData = ref(null)
const isLoading = ref(true)

const fetchSessionData = async (id) => {
  try {
    const response = await fetch(`http://localhost:8000/api/sessions/${id}/`)
    if (!response.ok) throw new Error('Session not found')

    sessionData.value = await response.json()
  } catch (error) {
    console.error("Error fetching session:", error)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  // Grab the UUID passed from the Review page router push
  const sessionId = route.query.id
  if (sessionId) {
    fetchSessionData(sessionId)
  } else {
    // Fallback if no ID is provided
    router.push('/')
  }
})

const goHome = () => {
  router.push('/')
}
</script>

<style scoped>
/* Keep existing header styles... */
.result-page {
  min-height: 100vh;
  background-color: #5B8FFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
.header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 30px;
}

.title {
  color: #FFD700;
  font-size: 2rem;
  margin: 0;
}

.header-logo { width: 200px; }
.result-layout {
  display: flex;
  gap: 40px;
  align-items: center;
}

.qr-section { text-align: center; }
.qr-placeholder { width: 150px; height: 150px; background: white; border: 2px solid #333; overflow: hidden; display: flex; align-items: center; justify-content: center; }
.qr-text { color: #FFD700; margin-top: 10px; font-weight: bold; }

.composite-frame {
  width: 600px;
  /* Remove the background-image CSS property since we now display the full composite image directly */
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
}

.final-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.home-btn { margin-top: 40px; padding: 15px 40px; border-radius: 30px; cursor: pointer; background-color: white; color: #4CAF50; font-size: 1.2rem; border: none; font-weight: bold; }
</style>
