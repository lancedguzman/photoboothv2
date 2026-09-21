import { defineStore } from 'pinia'
import { ref } from 'vue'

export const usePhotoStore = defineStore('photoStore', () => {
  // Array to hold the 4 base64 image strings
  const photos = ref([null, null, null, null])

  const setPhoto = (index, dataUrl) => {
    photos.value[index] = dataUrl
  }

  const clearPhotos = () => {
    photos.value = [null, null, null, null]
  }

  return { photos, setPhoto, clearPhotos }
})
