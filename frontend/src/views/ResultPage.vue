<template>
  <div class="result-page">
    <!-- Success header -->
    <h1 class="header">your GOOGLEY picture is ready!</h1>

    <div class="result-layout">
      <!-- QR Code Section -->
      <div class="qr-section">
        <div class="qr-placeholder">
          <!-- Django backend generated QR code image will render here -->
        </div>
        <p class="qr-text">get a digital copy</p>
      </div>

      <!-- Final Composite Frame -->
      <div class="composite-frame">
        <h2 class="frame-title">GOOGLEY WEEK</h2>
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
  height: 100vh;
  background-color: #5B8FFF;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
.header {
  color: #FFD700;
  margin-bottom: 30px;
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
}
.composite-frame {
  background: #89CFF0;
  padding: 20px;
  border: 4px solid #333;
  width: 500px;
}
.frame-title {
  text-align: right;
  color: #EA4335;
}
.frame-slots {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: space-between;
}
.final-photo {
  width: 48%;
  height: 120px;
  background: white;
}
.home-btn {
  margin-top: 40px;
  padding: 10px 30px;
  border-radius: 20px;
  cursor: pointer;
}
</style>
