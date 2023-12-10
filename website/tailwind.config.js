/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontSize: {
        '2xs': '.65rem',
        '3xs': '.55rem',
        '4xs': '.45rem',
        '5xs': '.35rem',
      },
      width: {
        '2xs': '10rem',
        '3xs': '8rem',
        '4xs': '6rem',
      },
      colors: {
        'dark': '#1a202c',
        'light': '#f7fafc',
      }
    },
  },
  plugins: [],
}

