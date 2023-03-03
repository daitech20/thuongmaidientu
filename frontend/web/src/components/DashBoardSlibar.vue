<template>
    <a-layout-sider v-model="collapsed">
        <div class="logo">
        </div>
        <a-menu theme="dark" mode="inline">
            <a-menu-item key="product.list" v-if="user && user.is_superuser">
                <gold-outlined/>
                <router-link class="menu-link" :to="{name: 'product.list'}">Products</router-link>
            </a-menu-item>
            <a-menu-item key="category.list" v-if="user && user.is_superuser">
                <gold-outlined/>
                <router-link class="menu-link" :to="{name: 'category.list'}">Categories</router-link>
            </a-menu-item>
            <a-menu-item key="brand.list" v-if="user && user.is_superuser">
                <gold-outlined/>
                <router-link class="menu-link" :to="{name: 'brand.list'}">Brands</router-link>
            </a-menu-item>
        </a-menu>
    </a-layout-sider>
</template>

<script>
import { mapActions } from 'pinia'
import { appearance } from '../store/appearance'
import BaseRequest from '../core/BaseRequest.js'
import { PieChartOutlined, UserOutlined, MessageOutlined, GoldOutlined, PayCircleOutlined, OrderedListOutlined } from '@ant-design/icons-vue'
export default {
    data() {
        return {
            selectedKeys: [],
            collapsed: false,
            errors: {
            }
        }
    },
    props: ['user'],
    mounted() {
        this.collapsed = this.isSidebarCollapased()
    },
    methods: {
        ...mapActions(appearance, ['isSidebarCollapased', 'setSidebarCollapsed']),
    },
    components: {
        PieChartOutlined, UserOutlined, MessageOutlined, GoldOutlined, PayCircleOutlined, OrderedListOutlined
    }
}
</script>

<style scoped>
.logo {
    width: 100%;
    padding: 16px 16px;
}
.logo-image {
   width: 100%;
   background-color: #fff;
}
.ant-menu-item .anticon + .menu-link {
    margin-left: 10px;
}
.ant-menu.ant-menu-inline-collapsed > .ant-menu-item .anticon + .menu-link {
    display: inline-block;
    opacity: 0;
}
</style>