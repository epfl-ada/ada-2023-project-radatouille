import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default ({ mode }) => {
  process.env = { ...process.env, ...loadEnv(mode, process.cwd()) };


  const BASE_URL = process.env.VITE_BASE_URL || ''


  return defineConfig({
    plugins: [vue()],
    base: `${BASE_URL}/`
  })

} 