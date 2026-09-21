<template>
  <div class="result-page">
    <!-- Background Clouds -->
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-top" alt="cloud" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-bottom" alt="cloud" />

    <div class="content-wrapper">
      <div class="header">
        <h1 class="title">your</h1>
        <img src="https://gdgloyola.pythonanywhere.com/media/assets/googley-logo.svg" alt="Googley" class="header-logo" />
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

      <!-- Updated Finish Button -->
      <button class="home-btn" @click="goHome">
        <img src="https://gdgloyola.pythonanywhere.com/media/assets/finish-button.svg" alt="Finish" class="finish-img" />
      </button>
    </div>
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
    const response = await fetch(`https://gdgloyola.pythonanywhere.com/api/sessions/${id}/`)
    if (!response.ok) throw new Error('Session not found')

    sessionData.value = await response.json()
  } catch (error) {
    console.error("Error fetching session:", error)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  const sessionId = route.query.id
  if (sessionId) {
    fetchSessionData(sessionId)
  } else {
    router.push('/')
  }
})

const goHome = () => {
  router.push('/')
}
</script>

<style scoped>
.result-page {
  position: relative;
  min-height: 100vh;
  background-color: #5B8FFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  overflow: hidden;
}
.cloud {
  position: absolute;
  z-index: 1;
  opacity: 0.8;
}
.cloud-top { top: 5%; right: 10%; width: 200px; }
.cloud-bottom { bottom: 10%; left: 5%; width: 250px; }

.content-wrapper {
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 30px;
}
.title { color: #FFD700; font-size: 2rem; margin: 0; }
.header-logo { width: 200px; }
.result-layout { display: flex; gap: 40px; align-items: center; }

.qr-section { text-align: center; }
.qr-placeholder { width: 150px; height: 150px; background: white; border: 2px solid #333; overflow: hidden; display: flex; align-items: center; justify-content: center; }
.qr-text { color: #FFD700; margin-top: 10px; font-weight: bold; }

.composite-frame {
  width: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
}
.final-img { width: 100%; height: 100%; object-fit: contain; }

/* Updated Button Styles */
.home-btn {
  margin-top: 40px;
  background: none;
  border: none;
  cursor: pointer;
  transition: transform 0.2s;
  padding: 0;
}
.home-btn:hover {
  transform: scale(1.05);
}
.finish-img {
  width: 200px;
}
</style>
