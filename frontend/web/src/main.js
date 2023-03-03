import { createApp } from 'vue'
import App from './App.vue'
// import 'ant-design-vue/dist/antd.css'
import { createPinia } from 'pinia'
import router from './routers'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'


const app = createApp(App)
app.use(createPinia())
app.use(Antd)
app.use(router)
app.mount('#app')
