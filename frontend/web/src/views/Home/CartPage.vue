<template>
    <!-- /HEADER -->
    <HomeHeader ref="Cart"/>
    
	<!-- BREADCRUMB -->
    <div id="breadcrumb" class="section">
			<!-- container -->
			<div class="container">
				<!-- row -->
				<div class="row">
					<div class="col-md-12">
						<h3 class="breadcrumb-header">Gio hang</h3>
						<ul class="breadcrumb-tree">
							<li>
								<router-link :to="{name: 'home'}">Home</router-link>
							</li>
							<li class="active">Gio hang</li>
						</ul>
					</div>
				</div>
				<!-- /row -->
			</div>
			<!-- /container -->
		</div>
	<!-- /BREADCRUMB -->

    <!-- SECTION -->
		<div class="section">
			<!-- container -->
			<div class="container">
                <a-table class="ant-table-striped" :columns="columns" :data-source="data" :scroll="{ x: 1000, y: 500 }" >
                    <template #bodyCell="{ column, record }">
                        <template v-if="column.dataIndex === 'image'">
                            <a-image
                                :width="50"
                                :src="record.image"
                            />
                        </template>
                        <template v-if="column.dataIndex === 'option'">
                            <a-button type="primary" danger size="small" @click="deleteCartProduct(record.id)">Delete</a-button>
                        </template>
                        <template v-if="column.dataIndex === 'quantity'">
                            <a-input-number v-model:value="record.quantity" :min="1" @change="updateProductQuantity(record.id)"/>
                        </template>
                    </template>
				</a-table>
                <div class="cart-summary">
                    <small>{{ carts.length }} Item(s) selected</small>
                    <h5>SUBTOTAL: {{ subtotal }} vnd</h5>
                </div>
</div>
			<!-- /container -->
		</div>
		<!-- /SECTION -->

    <HomeFooter/>

</template>

<script>
import authService from '../../services/tmdt/auth.service'
import { authStore } from '../../store/auth.store'
import { mapActions, mapState } from 'pinia';
import HomeHeader from '../../components/HomeHeader.vue'
import HomeFooter from '../../components/HomeFooter.vue'
import BaseRequest from '../../core/BaseRequest.js';
import { notification } from 'ant-design-vue';

export default {
    data() {
        return {
			carts: [],
			subtotal: 0,
            columns: [],
            data: [],
        }
    },
	components: {
        HomeHeader,
        HomeFooter
    },
	mounted() {
		this.getCarts()
	},
	computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    methods: {
        ...mapActions(authStore, ['setAccessToken', 'setUser', 'setRefreshToken']),
		showModalLogin: function() {
			this.visible_login = true
		},
		handleLogin: function() {
			this.$router.push({ name: 'login-register'});
		},
        getCarts: function(){
            this.columns = [
                {
				title: 'Id',
				dataIndex: 'id',
				key: 'id'
				},
				{
				title: 'ten sp',
				dataIndex: 'name',
				key: 'name'
				},
				{
				title: 'hinhanh',
				dataIndex: 'image',
				key: 'image'
				},
				{
				title: 'gia',
				dataIndex: 'price',
				key: 'price'
				},
                {
				title: 'so luong',
				dataIndex: 'quantity',
				key: 'quantity'
				},
                {
				title: 'Lựa chọn',
				dataIndex: 'option',
				key: 'option'
				},
			];

			if (this.user) {
				BaseRequest.get('orders/cart-list')
				.then(response => {
					this.carts = response.data
					console.log('cart', this.carts)
					for (const num in this.carts) {
						this.subtotal += this.carts[num].quantity * this.carts[num].product.price
                        this.data.push({
                            name: this.carts[num].product.name,
							image: this.carts[num].product.image,
							price: this.carts[num].product.price,
							quantity: this.carts[num].quantity,
							id: this.carts[num].id
						})
					}
				})
				.catch(error=> {
					this.errors = error.response.data
					console.log("error")
				});
			}
        },
        updateProductQuantity: function(cart_id) {
            var index = this.data.findIndex(d => d.id == cart_id);
            BaseRequest.patch('orders/cart-update/' + cart_id, {
                quantity: this.data[index].quantity,
                id: cart_id
            })
            .then(response => {
                this.$refs.Cart.getCarts()
                BaseRequest.get('orders/cart-list')
				.then(response => {
					this.carts = response.data
                    this.subtotal = 0
					for (const num in this.carts) {
						this.subtotal += this.carts[num].quantity * this.carts[num].product.price
					}
				})
				.catch(error=> {
					this.errors = error.response.data
					console.log("error")
				});
            })
            .catch(error=> {
                this.errors = error.response.data
                console.log("error")
            });
        },
        deleteCartProduct: function(cart_id) {
            BaseRequest.delete('orders/cart-update/' + cart_id)
            .then(response => {
                this.carts = response.data
                this.data = []
                this.getCarts()
                this.$refs.Cart.getCarts()
                BaseRequest.get('orders/cart-list')
				.then(response => {
					this.carts = response.data
                    this.subtotal = 0
					for (const num in this.carts) {
						this.subtotal += this.carts[num].quantity * this.carts[num].product.price
					}
				})
				.catch(error=> {
					this.errors = error.response.data
					console.log("error")
				});
				this.createSuccessNotification('xoa san pham thanh cong', 'thanh cong')
            })
            .catch(error=> {
                this.errors = error.response.data
                console.log("error")
            });
        },
		createSuccessNotification: function(message, description) {
            notification['success']({
                message: message,
                description: description,
            });
        },
    }
}
</script>

<style scoped>
</style>