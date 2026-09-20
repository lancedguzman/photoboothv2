<template>
  <div class="result-page">
    <div class="header">
      <h1 class="title">your</h1>
      <img src="http://localhost:8000/media/assets/googley-logo.svg" alt="Googley" class="header-logo" />
      <h1 class="title">picture is ready!</h1>
    </div>

    <div class="result-layout">
      <!-- QR Code Section -->
      <div class="qr-section">
        <div class="qr-placeholder">
          <!-- Django backend generated QR code image will render here -->
        </div>
        <p class="qr-text">get a digital copy</p>
      </div>

      <!-- Final Composite Frame applying ga-2026-frame.png -->
      <div class="composite-frame">
        <div class="frame-slots">
          <div v-for="index in 4" :key="index" class="final-photo"></div>
        </div>
      </div>
    </div>

    <button class="btn home-btn" @click="goHome">Finish</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goHome = () => {
  router.push('/')
}
</script>

<style scoped>
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
.header-logo {
  width: 200px;
}
.result-layout {
  display: flex;
  gap: 40px;
  align-items: center;
}
.qr-section {
  text-align: center;
}
.qr-placeholder {
  width: 150px;
  height: 150px;
  background: white;
  border: 2px solid #333;
}
.qr-text {
  color: #FFD700;
  margin-top: 10px;
  font-weight: bold;
}
.composite-frame {
  /* Use the frame image as the background */
  background-image: url('http://localhost:8000/media/frame/ga-2026-frame.png');
  background-size: cover;
  background-position: center;
  width: 600px;
  height: 400px;
  padding: 40px;
  box-sizing: border-box;
  display: flex;
  align-items: flex-end; /* Aligns photos to bottom if frame design dictates */
}
.frame-slots {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: space-between;
  width: 100%;
}
.final-photo {
  width: 45%;
  height: 120px;
  background: white;
  opacity: 0.8; /* Placeholder opacity to see the frame behind it */
}
.home-btn {
  margin-top: 40px;
  padding: 15px 40px;
  border-radius: 30px;
  cursor: pointer;
  background-color: white;
  color: #4CAF50;
  font-size: 1.2rem;
  border: none;
  font-weight: bold;
}
</style>
