import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    watch: {
      usePolling: true,
    },
    hmr: {
      protocol: 'ws',
      clientPort: 3000,
    },
  },
})


// // vite.config.js
// import { defineConfig } from 'vite'
// import react from '@vitejs/plugin-react'
// import path from 'path'

// export default defineConfig({
//   plugins: [react()],
//   // esbuild: {
//   //   loader: 'tsx', // change this to 'tsx'
//   //   include: /\.[jt]sx?$/, // change this to handle both .jsx and .tsx files
//   //   exclude: [],
//   // },
//   build: {
//     sourcemap: true, // Enable source maps
//   },
//   server: {
//     host: '0.0.0.0',
//     port: 3000,
//     watch: {
//       usePolling: true,
//     },
//     hmr: {
//       protocol: 'ws',
//       clientPort: 3000,
//     },
//   },
//   root: path.resolve(__dirname, 'src'),
//   publicDir: path.resolve(__dirname, 'public'),
// })