<template>
    <header>
			<!-- TOP HEADER -->
			<div id="top-header">
				<div class="container">
					<ul class="header-links pull-right">
						<li v-if="user != null" >
							<a><i class="fa fa-user-o"></i> {{ user.email }} </a>

							<router-link :to="{ name: 'dashboard'}" >
								<a> DashBoard </a>
							</router-link>   

							<a @click="handleLogout"> Logout </a>
						</li>
						<li v-else>
							<router-link :to="{ name: 'login-register'}" >
								<a> Login</a>
							</router-link>   
						</li>
					</ul>
				</div>
			</div>
			<!-- /TOP HEADER -->

            <!-- MAIN HEADER -->
			<div id="header">
				<!-- container -->
				<div class="container">
					<!-- row -->
					<div class="row">
						<!-- LOGO -->
						<div class="col-md-3">
							<div class="header-logo">
								<a href="#" class="logo">
									<img src="./img/logo.png" alt="">
								</a>
							</div>
						</div>
						<!-- /LOGO -->

                        <!-- SEARCH BAR -->
						<div class="col-md-6">
							<div class="header-search">
								<form>
									<select class="input-select">
										<option value="0">All Categories</option>
										<option value="1">Category 01</option>
										<option value="1">Category 02</option>
									</select>
									<input class="input" placeholder="Search here">
									<button class="search-btn">Search</button>
								</form>
							</div>
						</div>
						<!-- /SEARCH BAR -->

                        <!-- ACCOUNT -->
						<div class="col-md-3 clearfix">
							<div class="header-ctn">
                                <!-- Cart -->
								<div class="dropdown">
									<a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="true">
										<i class="fa fa-shopping-cart"></i>
										<span>Your Cart</span>
										<div class="qty">{{ carts.length }}</div>
									</a>
									<div class="cart-dropdown">
										<div class="cart-list" v-if="this.user">
											<div v-for="cart in carts" class="product-widget">
												<div class="product-img">
													<img :src="cart.product.image" alt="">
												</div>
												<div class="product-body">
													<h3 class="product-name"><a href="#">{{ cart.product.name }}</a></h3>
													<h4 class="product-price"><span class="qty">{{ cart.quantity }}x</span>{{ cart.quantity * cart.product.price }} vnd</h4>
												</div>
												<button class="delete"><i class="fa fa-close"></i></button>
											</div>
										</div>
										<div class="cart-summary">
											<small>{{ carts.length }} Item(s) selected</small>
											<h5>SUBTOTAL: {{ subtotal }} vnd</h5>
										</div>
										<div class="cart-btns">
											<router-link :to="{name: 'cart.detail'}">View Cart</router-link>
											<router-link :to="{name: 'checkout'}">Checkout</router-link>
											<i class="fa fa-arrow-circle-right"></i>
										</div>
									</div>
								</div>
								<!-- /Cart -->

                                <!-- Menu Toogle -->
								<div class="menu-toggle">
									<a href="#">
										<i class="fa fa-bars"></i>
										<span>Menu</span>
									</a>
								</div>
								<!-- /Menu Toogle -->
							</div>
						</div>
						<!-- /ACCOUNT -->
					</div>
					<!-- row -->
				</div>
				<!-- container -->
			</div>
			<!-- /MAIN HEADER -->
		</header>
		<!-- /HEADER -->

</template>

<script>
import { authStore } from '../store/auth.store'
import { mapActions, mapState } from 'pinia';
import BaseRequest from '../core/BaseRequest.js';

export default {
    data() {
        return {
			carts: [],
			subtotal: 0,
        }
    },
	computed: {
        ...mapState(authStore, ['user'])
    },
	mounted() {
		this.getCarts()
	},
    methods: {
		...mapActions(authStore, ['clearAccessToken', 'clearUser', 'clearRefreshToken']),
		handleLogout: function() {
            this.clearAccessToken()
            this.clearRefreshToken()
            this.clearUser()
            this.$router.push({path: 'login-register'})
        },
		getCarts: function(){
			if (this.user) {
				BaseRequest.get('orders/cart-list')
				.then(response => {
					this.carts = response.data
					for (const num in this.carts) {
						this.subtotal += this.carts[num].quantity * this.carts[num].product.price
					}
				})
				.catch(error=> {
					this.errors = error.response.data
					console.log("error")
				});
			}
        },

    }
}
</script>

<style scoped>
</style>