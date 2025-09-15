import { createRouter, createWebHistory } from "vue-router"
import DataPage from "../components/pages/Data.vue"
import SleepPage from "../components/pages/Sleep.vue"
import MainPage from "../components/pages/Main.vue"

const routes = [
  {
    path: '/', component: MainPage
  },
  {
    path: '/data', component: DataPage
  },
  {
    path: '/sleep', component: SleepPage 
  }
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})