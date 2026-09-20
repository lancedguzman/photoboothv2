<template>
  <div class="capture-page">
    <div class="main-layout">

      <!-- Main camera view -->
      <div class="camera-feed">
        <h2>live view from camera</h2>
      </div>

      <!-- Sidebar for 4 thumbnails -->
      <div class="thumbnail-sidebar">
        <div v-for="index in 4" :key="index" class="thumbnail-slot">
          <!-- Refresh icon button for individual retakes -->
          <button class="refresh-icon">↻</button>
        </div>
      </div>
    </div>

    <!-- Main capture trigger -->
    <div class="controls">
      <button class="capture-btn" @click="capturePhoto">capture</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const capturePhoto = () => {
  // Logic to capture 4 photos sequentially would go here
  // After capturing 4 photos, push to review page
  router.push('/review')
}
</script>

<style scoped>
.capture-page {
  height: 100vh;
  background-color: #5B8FFF;
  display: flex;
  flex-direction: column;
  padding: 20px;
}
.main-layout {
  display: flex;
  flex: 1;
  gap: 20px;
  justify-content: center;
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
}
.capture-btn {
  padding: 15px 50px;
  font-size: 24px;
  color: #4CAF50;
  background: white;
  border-radius: 30px;
}
</style>
