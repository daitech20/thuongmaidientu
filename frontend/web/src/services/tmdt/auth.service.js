import http from './http.service'

export default {
    login(email, password) {
        return http.post('/api/users/token/', {
            email: email,
            password: password
        });
    },

    logout() {
        return http.post('/api/logout');
    },

    refreshToken(refreshToken) {
        return http.post('/api/users/token/refresh/', {
            refresh: refreshToken
        });
    },

    checkExpriedToken(username) {
        return http.get('/api/user/' + username)
    }
 }