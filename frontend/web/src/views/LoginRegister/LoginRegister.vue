<template>
    <!-- /HEADER -->
    <HomeHeader/>      
  <a-form
    :model="credentials"
    name="basic"
    :label-col="{ span: 8 }"
    :wrapper-col="{ span: 8 }"
    autocomplete="off"
    @finish="login"
    style="margin-top: 100px;"
  >
    <a-form-item
      label="Email"
      name="email"
      :rules="[{ required: true, message: 'Please input your email!' }]"
    >
      <a-input v-model:value="credentials.email" />
    </a-form-item>
    <a-form-item
      label="Password"
      name="password"
      :rules="[{ required: true, message: 'Please input your password!' }]"
    >
      <a-input-password v-model:value="credentials.password" />
    </a-form-item>

    <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
      <a-button type="primary" html-type="submit">Submit</a-button>
    </a-form-item>
  </a-form>

    <HomeFooter/>

</template>

<script>
import authService from '../../services/tmdt/auth.service'
import { authStore } from '../../store/auth.store'
import { mapActions } from 'pinia';
import HomeHeader from '../../components/HomeHeader.vue'
import HomeFooter from '../../components/HomeFooter.vue'
import { notification } from 'ant-design-vue';


export default {
    data() {
        return {
            credentials: {
                email: "",
                password: ""
            },
            errors: {}
        }
    },
    methods: {
        ...mapActions(authStore, ['setAccessToken', 'setUser', 'setRefreshToken', 'setProfile']),
        login() {
            authService.login(this.credentials.email, this.credentials.password).then(response => {
              console.log(response.data)  
              this.setAccessToken(response.data.access);
                this.setRefreshToken(response.data.refresh);
                this.setUser(response.data.user);
                this.setProfile(response.data.profile);
                this.$router.push({name: 'home'});
            }).catch(error => {
                this.errors = error.response.data;
                console.log(this.errors)
                this.errorsNotification('dang nhap that bai', 'sai mat khau')
            });
        },
        errorsNotification: function(message, description) {
            notification['error']({
                message: message,
                description: description,
            });
        }
    },
    components: {
        HomeHeader,
        HomeFooter
    }
}
</script>

<style scoped>

</style>