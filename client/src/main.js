import Vue from 'vue'
import App from './App.vue'
import addIcons from './utils/icons.js'
import 'bootstrap'; 
import 'bootstrap/dist/css/bootstrap.min.css';

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

addIcons(library)

Vue.component('icon', FontAwesomeIcon)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
