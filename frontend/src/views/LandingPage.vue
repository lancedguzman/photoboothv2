<template>
  <div class="landing-page">
    <!-- Background Clouds -->
    <img src="http://localhost:8000/media/assets/cloud-1.svg" class="cloud cloud-1" alt="cloud" />
    <img src="http://localhost:8000/media/assets/cloud-2.svg" class="cloud cloud-2" alt="cloud" />
    <img src="http://localhost:8000/media/assets/cloud-3.svg" class="cloud cloud-3" alt="cloud" />

    <div class="content-wrapper">
      <h1 class="title">capture your</h1>
      <img src="http://localhost:8000/media/assets/googley-logo.svg" alt="Googley Logo" class="logo" />
      <h1 class="title">moment!</h1>

      <!-- Replaced standard button with custom SVG button -->
      <button class="start-btn" @click="goToCapture">
        <img src="http://localhost:8000/media/assets/start-button.svg" alt="Start" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goToCapture = () => {
  router.push('/capture')
}
</script>

<style scoped>
.landing-page {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #5B8FFF;
  text-align: center;
  overflow: hidden;
}
.content-wrapper {
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.title {
  color: #FFD700;
  font-family: sans-serif;
  margin: 0;
  font-size: 2rem;
}
.logo {
  width: 300px;
  margin: 10px 0;
}
.start-btn {
  background: none;
  border: none;
  cursor: pointer;
  margin-top: 20px;
  transition: transform 0.2s;
}
.start-btn:hover {
  transform: scale(1.05);
}
.cloud {
  position: absolute;
  z-index: 1;
  opacity: 0.9;
}
.cloud-1 { top: 10%; left: 5%; width: 150px; }
.cloud-2 { top: 20%; right: 10%; width: 200px; }
.cloud-3 { bottom: 15%; left: 20%; width: 180px; }
</style>
