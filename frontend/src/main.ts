import { createApp } from 'vue'

import '@fontsource/iosevka/100.css'
import '@fontsource/iosevka/300.css'
import '@fontsource/iosevka/400.css'
import '@fontsource/iosevka/500.css'
import '@fontsource/iosevka/700.css'
import '@fontsource/iosevka/900.css'

import '@fontsource/roboto/100.css'
import '@fontsource/roboto/300.css'
import '@fontsource/roboto/400.css'
import '@fontsource/roboto/500.css'
import '@fontsource/roboto/700.css'
import '@fontsource/roboto/900.css'

// Components
import App from './App.vue'
import { router } from './plugins/routes'
import { vuetify } from './plugins/vuetify'

createApp(App)
  .use(vuetify)
  .use(router)
  .mount('#app')
