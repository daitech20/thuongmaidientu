<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
        <DashBoardSlibar :user="user" />
        <a-layout>
            <DashBoardHeader/>
                <a-layout-content class="content">
                    <router-view v-slot="{ Component }">
                        <!-- <transition> -->
                            <component :is="Component" />
                        <!-- </transition> -->
                    </router-view>
                </a-layout-content>
            <DashBoardFooter/>
        </a-layout>
    </a-layout>
</template>

<script>
import DashBoardSlibar from '../../components/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoardFooter.vue'
import { authStore } from '../../store/auth.store'
import { mapState } from 'pinia'


export default {
    data() {
        return {
        }
    },
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter
    },
    computed: {
        ...mapState(authStore, ['isLoggedIn', 'user'])
    }
    
}
</script>