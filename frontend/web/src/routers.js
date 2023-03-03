import { createRouter, createWebHistory } from "vue-router"
import { authStore } from "./store/auth.store"
import HomePage from './views/Home/HomePage.vue'
import LoginRegister from './views/LoginRegister/LoginRegister.vue'
import DashBoard from './views/DashBoard/DashBoard.vue'
// import LoginPage from './views/login/LoginPage.vue'
// import DashboardPage from './views/DashboardPage.vue'
import ProductListPage from './views/Product/ProductListPage.vue'
import ProductDetailPage from './views/Product/ProductDetailPage.vue'
import ProductCreatePage from './views/Product/ProductCreatePage.vue'
import CategoryListPage from './views/Category/CategoryListPage.vue'
import CategoryCreatePage from './views/Category/CategoryCreatePage.vue'
import CategoryDetailPage from './views/Category/CategoryDetailPage.vue'
import BrandListPage from './views/Brand/BrandListPage.vue'
import BrandDetailPage from './views/Brand/BrandDetailPage.vue'
import BrandCreatePage from './views/Brand/BrandCreatePage.vue'
import CartPage from './views/Home/CartPage.vue'
import CheckoutPage from './views/Home/CheckoutPage.vue'
// import PaymentListPage from './views/payment/PaymentListPage.vue'
// import AccountListPage from './views/account/AccountListPage.vue'
// import AccountCreatePage from './views/account/AccountCreatePage.vue'
// import AccountDetailPage from './views/account/AccountDetailPage.vue'
// import AccountChangePasswordPage from './views/account/AccountChangePasswordPage.vue'
// import AccountResetPasswordPage from './views/account/AccountResetPasswordPage.vue'
// import OrderListPage from './views/order/OrderListPage.vue'
// import OrderDetailPage from './views/order/OrderDetailPage.vue'

const routes = [
    {
        name: 'home',
        path: '/',
        component: HomePage
    },
    {
        name: 'login-register',
        path: '/login-register',
        component: LoginRegister
    },
    {
        name: 'dashboard',
        path: '/dashboard',
        component: DashBoard,
        params: true
    },
    {
        name: 'product.list',
        path: '/dashboard/products',
        component: ProductListPage,
        params: true
    },
    {
        name: 'product.create',
        path: '/dashboard/product/create',
        component: ProductCreatePage,
        params: true
    },
    {
        name: 'product.detail',
        path: '/dashboard/product/detail/:product_id',
        component: ProductDetailPage,
        params: true
    },
    {
        name: 'category.list',
        path: '/dashboard/categories',
        component: CategoryListPage,
        params: true
    },
    {
        name: 'category.create',
        path: '/dashboard/category/create',
        component: CategoryCreatePage,
        params: true
    },
    {
        name: 'category.detail',
        path: '/dashboard/category/detail/:category_id',
        component: CategoryDetailPage,
        params: true
    },
    {
        name: 'brand.list',
        path: '/dashboard/brands',
        component: BrandListPage,
        params: true
    },
    {
        name: 'brand.create',
        path: '/dashboard/brand/create',
        component: BrandCreatePage,
        params: true
    },
    {
        name: 'brand.detail',
        path: '/dashboard/brand/detail/:brand_id',
        component: BrandDetailPage,
        params: true
    },
    {
        name: 'cart.detail',
        path: '/carts',
        component: CartPage,
        params: true
    },
    {
        name: 'checkout',
        path: '/checkout',
        component: CheckoutPage,
        params: true
    },
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes // short for `routes: routes`
})

export default router