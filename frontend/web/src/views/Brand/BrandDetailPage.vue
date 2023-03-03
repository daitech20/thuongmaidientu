<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar :user="user" />
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Chi tiết brand"
                sub-title="" />
                <a-layout-content style="padding: 0 50px">
                    <a-form
                        :model="brand"
                        name="nest-messages"
                        :label-col="{ span: 4 }"
                        :wrapper-col="{ span: 16 }"
                        @finish="onFinish"
                    >
                        <a-form-item
                            :name="['name']"
                            label="Tên sản phẩm"
                            :rules="[{ required: true, message: 'Vui lòng nhập tên brand!' }]"
                            :validateStatus="errors.name ? 'error': ''"
                        >
                            <a-input v-model:value="brand.name" />
                            <a-typography-text v-if="errors.name" type="danger">
                                {{errors.name[0]}}
                            </a-typography-text>
                        </a-form-item>
                        
                        <a-form-item
                            :name="['description']"
                            label="Mô tả"
                            :rules="[{ required: true, message: 'Vui lòng nhập mô tả!' }]"
                        >
                            <a-input v-model:value="brand.description" />
                        </a-form-item>

                        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
                            <a-button type="primary" html-type="submit" >Cập nhật</a-button>
                        </a-form-item>
                    </a-form>
                </a-layout-content>
            </a-layout>
            <DashBoardFooter/>
		</a-layout>
	</a-layout>
</template>

<script lang="ts">
import BaseRequest from '../../core/BaseRequest.js'
import { notification } from 'ant-design-vue';
import { defineComponent, ref } from 'vue';
import type { UploadProps, UploadChangeParam } from 'ant-design-vue';
import { UploadOutlined } from '@ant-design/icons-vue';
import DashBoardSlibar from '../../components/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoardFooter.vue'
import { authStore } from '../../store/auth.store';
import { mapState } from 'pinia';

export default({
    data() {
        return {
            brand: {
                name: '',
                description: '',
            },
            errors: {},
        }
    },
    mounted() {
        this.getData()
    },
    computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    methods: {
        getData: function() {
            BaseRequest.get('products/brand/' + this.$route.params.brand_id)
			.then(response => {
				this.brand.name = response.data.name
                this.brand.description = response.data.description
			})
			.catch(error=> {
				this.errors = error.response.data
			});
        },
        onFinish: function() {
            BaseRequest.put('products/brand/' + this.$route.params.brand_id, {
                name: this.brand.name,
                description: this.brand.description,
            })
            .then(response => {
                    this.errors = {}
                    this.updateSuccessNotification()
                    this.$router.push({ name: 'brand.list'});
                }
            )
            .catch(error=> {
                this.errors = error.response.data
                console.log(this.errors)
            });
        },
        updateSuccessNotification: function() {
            notification['success']({
                message: 'Update successfully!',
                description:
                'Brand was updated! ',
            });
        }
    },
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter, UploadOutlined
    },
})
</script>