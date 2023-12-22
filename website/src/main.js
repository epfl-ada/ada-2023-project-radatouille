import { createApp } from 'vue'
import './index.css'
import App from './App.vue'
import VueMathjax from 'vue-mathjax'

const app = createApp(App)
app.use(VueMathjax)
app.mount('#app')
