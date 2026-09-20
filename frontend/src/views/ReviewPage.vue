<template>
  <div class="review-page">
    <h1>Review Your Photos</h1>

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
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const retakeAll = () => {
  router.push('/capture')
}

const submitToBackend = async () => {
  // Axios/Fetch POST request to Django api/sessions/create/ goes here
  // Assuming successful upload:
  router.push('/result')
}
</script>

<style scoped>
.review-page {
  min-height: 100vh;
  background-color: #5B8FFF;
  text-align: center;
  padding: 20px;
  color: white;
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
}
</style>
