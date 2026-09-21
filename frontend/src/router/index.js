import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/LandingPage.vue'
import CapturePage from '../views/CapturePage.vue'
import ResultPage from '../views/ResultPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingPage,
    },
    {
      path: '/capture',
      name: 'capture',
      component: CapturePage,
    },
    {
      path: '/result',
      name: 'result',
      component: ResultPage,
    },
  ],
})

export default router
