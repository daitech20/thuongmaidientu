<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar :user="user" />
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Chi tiết sản phẩm"
                sub-title="" />
                <a-layout-content style="padding: 0 50px">
                    <a-form
                        :model="product"
                        name="nest-messages"
                        :label-col="{ span: 4 }"
                        :wrapper-col="{ span: 16 }"
                        @finish="onFinish"
                    >
                        <a-form-item
                            :name="['name']"
                            label="Tên sản phẩm"
                            :rules="[{ required: true, message: 'Vui lòng nhập tên sản phẩm!' }]"
                            :validateStatus="errors.name ? 'error': ''"
                        >
                            <a-input v-model:value="product.name" />
                            <a-typography-text v-if="errors.name" type="danger">
                                {{errors.name[0]}}
                            </a-typography-text>
                        </a-form-item>
                        
                        <a-form-item
                            :name="['description']"
                            label="Mô tả"
                            :rules="[{ required: true, message: 'Vui lòng nhập mô tả!' }]"
                        >
                            <a-input v-model:value="product.description" />
                        </a-form-item>

                        <a-form-item :name="['image']" label="Hình ảnh" :rules="[{ required: false }]">
                            <a-image
                                :width="200"
                                :src="product.image"
                            />
                            <a-upload
                                v-model:file-list="fileList"
                                list-type="picture"
                                :max-count="1"
                                accept=".jpg,.png"
                                >
                                <a-button>
                                    <upload-outlined></upload-outlined>
                                    Upload (Max: 1)
                                </a-button>
                            </a-upload>
                        </a-form-item>
                        
                        <a-form-item
                            :name="['category']"
                            label="Category"
                        >
                            <a-select
                                v-model:value="value_category"
                                label-in-value
                                style="width: 120px"
                                :options="options_category"
                            ></a-select>
                        </a-form-item>

                        <a-form-item
                            :name="['brand']"
                            label="Brand"
                        >
                            <a-select
                                v-model:value="value_brand"
                                label-in-value
                                style="width: 120px"
                                :options="options_brand"
                            ></a-select>
                        </a-form-item>

                        <a-form-item
                            :name="['price']"
                            label="Giá"
                            :rules="[{ required: true, message: 'Vui lòng nhập giá tiền!' }]"
                        >
                            <a-input v-model:value="product.price" />
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
            product: {
                name: '',
                description: '',
                image: '',
                price: '',
                category: '',
                brand: '',
            },
            categories: {},
            brands: {},
            options_category: [],
            value_category: {},
            options_brand: [],
            value_brand: {},
            errors: {},
            fileList: [],
        }
    },
    mounted() {
        this.getData()
    },
    computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    methods: {
        handleChange: function(info: UploadChangeParam) {
            this.product.image = this.fileList[0].thumbUrl
        },

        getData: function() {
            BaseRequest.get('products/category-list/')
			.then(response => {
				this.categories = response.data
                console.log(this.categories)
                for (let ct in this.categories) {
                    this.options_category.push(
                        {
                            value: this.categories[ct].id,
                            label: this.categories[ct].name
                        }
                    )
                }
                this.value_category = this.options_category[0]
                console.log(this.options_category)
			})
			.catch(error=> {
				this.errors = error.response.data
			});

            BaseRequest.get('products/brand-list/')
			.then(response => {
				this.brands = response.data
                console.log(this.brands)
                for (let br in this.brands) {
                    this.options_brand.push(
                        {
                            value: this.brands[br].id,
                            label: this.brands[br].name
                        }
                    )
                }
                this.value_brand = this.options_brand[0]
			})
			.catch(error=> {
				this.errors = error.response.data
			});

            BaseRequest.get('products/product/' + this.$route.params.product_id)
            .then(response => {
                    this.product.name = response.data.name,
                    this.product.description = response.data.description
                    this.product.image = response.data.image
                    this.product.price = response.data.price
                    this.product.category = response.data.category
                    this.product.brand = response.data.brand

                    for (let b in this.options_brand) {
                        if (this.options_brand[b].value == this.product.brand) {
                            this.value_brand = this.options_brand[b]
                        }
                    }

                    for (let c in this.options_category) {
                        if (this.options_category[c].value == this.product.category) {
                            this.value_category = this.options_category[c]
                        }
                    }
                }
            ).catch(error => {
                console.log("error")
            })
        },
        onFinish: function() {
            if (this.fileList[0] != null) {
                BaseRequest.put('products/product/' + this.$route.params.product_id, {
                    name: this.product.name,
                    description: this.product.description,
                    price: this.product.price,
                    image: this.fileList[0].thumbUrl,
                    category: this.value_category.value,
                    brand: this.value_brand.value,
                })
                .then(response => {
                        this.errors = {}
                        this.updateSuccessNotification()
                        this.$router.push({ name: 'product.list'});
                    }
                )
                .catch(error=> {
                    this.errors = error.response.data
                    console.log(this.errors)
                });
            }
            else {
                BaseRequest.put('products/product/' + this.$route.params.product_id, {
                    name: this.product.name,
                    description: this.product.description,
                    price: this.product.price,
                    category: this.value_category.value,
                    brand: this.value_brand.value,
                })
                .then(response => {
                        this.errors = {}
                        this.updateSuccessNotification()
                        this.$router.push({ name: 'product.list'});
                    }
                )
                .catch(error=> {
                    this.errors = error.response.data
                    console.log(this.errors)
                });
            }
            
        },
        updateSuccessNotification: function() {
            notification['success']({
                message: 'Update successfully!',
                description:
                'Product was updated! ',
            });
        }
    },
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter, UploadOutlined
    },
})
</script>
1