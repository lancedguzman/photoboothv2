<template>
  <div class="landing-page">
    <!-- Top Left GDG Logo -->
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/gdg-logo.svg" class="gdg-logo" alt="GDG Logo" />

    <!-- Background Clouds -->
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-tl" alt="cloud" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-tr" alt="cloud" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-mr" alt="cloud" />
    <img src="https://gdgloyola.pythonanywhere.com/media/assets/cloud.svg" class="cloud cloud-bl" alt="cloud" />

    <!-- Center Title Image -->
    <div class="content-wrapper">
      <img src="https://gdgloyola.pythonanywhere.com/media/assets/title.svg" class="main-title" alt="Capture your Googley moment!" />
    </div>

    <!-- Bottom Right Controls -->
    <div class="controls-wrapper">
      <img src="https://gdgloyola.pythonanywhere.com/media/assets/googley-left.svg" class="android-mascot" alt="Android Mascot" />
      <button class="start-btn" @click="goToCapture">
        <img src="https://gdgloyola.pythonanywhere.com/media/assets/start-button.svg" alt="Start" />
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
  overflow: hidden;
}

/* Top Left Logo Layout */
.gdg-logo {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 90px;
  z-index: 10;
}

/* Center Layout */
.content-wrapper {
  z-index: 10;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.main-title {
  width: 80%;
  max-width: 850px;
}

/* Bottom Right Controls Layout */
.controls-wrapper {
  position: absolute;
  bottom: 8%;
  right: 12%;
  display: flex;
  align-items: flex-end;
  z-index: 15;
}

.android-mascot {
  width: 110px;
  transform: translateY(15px); /* Creates the peeking effect */
  margin-right: -15px; /* Pulls the mascot slightly behind/into the start button */
  z-index: 16;
}

.start-btn {
  background: none;
  border: none;
  cursor: pointer;
  transition: transform 0.2s;
  width: 220px;
  z-index: 15;
}

.start-btn img {
  width: 100%;
}

.start-btn:hover {
  transform: scale(1.05);
}

/* Decorative Background Clouds */
.cloud {
  position: absolute;
  z-index: 1;
}

.cloud-tl { top: 12%; left: 5%; width: 280px; }
.cloud-tr { top: -5%; right: 5%; width: 200px; }
.cloud-mr { top: 45%; right: -5%; width: 140px; }
.cloud-bl { bottom: -8%; left: 10%; width: 350px; }
</style>
