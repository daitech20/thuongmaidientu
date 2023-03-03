<template>
<!-- FOOTER -->
    <footer id="footer">
        <!-- top footer -->
        <div class="section">
            <!-- container -->
            <div class="container">
                <!-- row -->
                <div class="row">
                   
                </div>
                <!-- /row -->
            </div>
            <!-- /container -->
        </div>
        <!-- /top footer -->
    </footer>
<!-- /FOOTER -->
</template>

<script>
import { authStore } from '../store/auth.store'

import { mapActions } from 'pinia';
export default {
    data() {
        return {

        }
    },
    methods: {
        ...mapActions(authStore, ['setAccessToken', 'setUser', 'setRefreshToken']),
    },
    components: {
        // UserOutlined, UnlockOutlined
    }
}
</script>

<style scoped>
</style>