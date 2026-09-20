<template>
  <div class="review-page">
    <img src="http://localhost:8000/media/assets/cloud-3.svg" class="cloud cloud-bg" alt="cloud" />

    <div class="content-wrapper">
      <h1 class="header-text">Review Your Photos</h1>

      <div class="photos-grid">
        <div v-for="index in 4" :key="index" class="photo-preview">
          <p>Photo {{ index }}</p>
        </div>
      </div>

      <div class="actions">
        <button class="btn secondary" @click="retakeAll">Retake All</button>
        <button class="btn primary" @click="submitToBackend">Print & Generate</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const retakeAll = () => {
  router.push('/capture')
}

const submitToBackend = async () => {
  router.push('/result')
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
}
.photos-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  max-width: 600px;
  margin: 20px auto;
}
.photo-preview {
  background: #ccc;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
}
.btn {
  padding: 15px 30px;
  margin: 0 10px;
  font-size: 18px;
  border-radius: 20px;
  cursor: pointer;
  border: none;
  font-weight: bold;
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
