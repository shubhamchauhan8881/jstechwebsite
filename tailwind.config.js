/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
  ],
  theme: {
    extend: {
      colors:{
        'primary': '#111B47',
        'secondary': '#1F2845',
        'primary-content': '#505F98',
        'secndary-content': '',
      },
      fontFamily: {
        'racing': "Racing Sans One, sans-serif",
        "poppins":  "Poppins, sans-serif",
        "roboto":  "Roboto, sans-serif"
      },
    },
  },
  plugins: [  require('@tailwindcss/forms')],
}

