<template>
	<div>
    <router-view v-slot="{ Component }">
        <!-- <transition> -->
            <component :is="Component" />
        <!-- </transition> -->
    </router-view>
  </div>
</template>

<script>
// import SideBar from './components/SideBar.vue'
// import Header from './components/Header.vue'
// import Footer from './components/Footer.vue'
import { authStore } from './store/auth.store'
import { mapState } from 'pinia'

export default {
    data() {
        return {
        }
    },
    computed: {
        ...mapState(authStore, ['isLoggedIn', 'user'])
    }
    
}

</script>


<style scoped>
.content {
    margin: 0 16px;
}
</style>
1