<template>
  <div class="landing-page">
    <div class="content-wrapper">
      <!-- Title text from prototype -->
      <h1 class="title">capture your GOOGLEY moment!</h1>

      <!-- Start button routes to the Capture page -->
      <button class="start-btn" @click="goToCapture">start</button>
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
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #5B8FFF; /* Base blue from prototype */
  text-align: center;
}
.title {
  color: #FFD700;
  font-family: sans-serif;
}
.start-btn {
  padding: 10px 40px;
  font-size: 24px;
  color: #4CAF50;
  background: white;
  border-radius: 30px;
  cursor: pointer;
}
</style>
