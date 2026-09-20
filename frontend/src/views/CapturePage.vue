<template>
  <div class="capture-page">
    <img src="http://localhost:8000/media/assets/cloud-2.svg" class="cloud cloud-top" alt="cloud" />

    <div class="main-layout">
      <div class="camera-feed">
        <h2>live view from camera</h2>
      </div>

      <div class="thumbnail-sidebar">
        <div v-for="index in 4" :key="index" class="thumbnail-slot">
          <button class="refresh-icon">↻</button>
        </div>
      </div>
    </div>

    <div class="controls">
      <button class="capture-btn" @click="capturePhoto">
        <img src="http://localhost:8000/media/assets/capture-button.svg" alt="Capture" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const capturePhoto = () => {
  router.push('/review')
}
</script>

<style scoped>
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
  gap: 20px;
  justify-content: center;
  z-index: 10;
}
.camera-feed {
  flex: 0.7;
  background: white;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.thumbnail-sidebar {
  flex: 0.2;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.thumbnail-slot {
  flex: 1;
  background: white;
  border-radius: 10px;
  position: relative;
}
.refresh-icon {
  position: absolute;
  top: 5px;
  right: 5px;
  color: red;
  background: none;
  border: none;
  cursor: pointer;
}
.controls {
  text-align: center;
  margin-top: 20px;
  z-index: 10;
}
.capture-btn {
  background: none;
  border: none;
  cursor: pointer;
  transition: transform 0.2s;
}
.capture-btn:hover {
  transform: scale(1.05);
}
</style>
