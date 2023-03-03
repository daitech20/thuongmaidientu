<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar :user="user" />
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Thêm sản phẩm"
                sub-title="This is a subtitle of detail product page" />
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

                        <a-form-item :name="['image']" label="Hình ảnh" >
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
                            <a-typography-text v-if="errors.price" type="danger">
                                {{errors.price[0]}}
                            </a-typography-text>
                        </a-form-item>

                        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
                            <a-button type="primary" html-type="submit" >Thêm</a-button>
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
import { authStore } from '../../store/auth.store';
import { mapState } from 'pinia';
import { defineComponent, ref } from 'vue';
import type { UploadProps, UploadChangeParam } from 'ant-design-vue';
import { UploadOutlined } from '@ant-design/icons-vue';
import DashBoardSlibar from '../../components/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoardFooter.vue'


export default({
    data() {
        return {
            product: {
                name: '',
                description: '',
                image: '',
                price: '',
            },
            categories: {},
            brands: {},
            options_category: [],
            value_category: {},
            options_brand: [],
            value_brand: {},
            errors: {},
            fileList: [],
            headers: {
                authorization: 'authorization-text',
            },
        }
    },
    mounted() {
        this.getData()
    },
    computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter, 
    },
    methods: {
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
        },
        handleChange: function(info: UploadChangeParam) {
            let resFileList = [...info.fileList];

            // 1. Limit the number of uploaded files
            //    Only to show two recent uploaded files, and old ones will be replaced by the new
            resFileList = resFileList.slice(-2);

            // 2. read from response and show file link
            resFileList = resFileList.map(file => {
            if (file.response) {
                // Component will show file.url as link
                file.url = file.response.url;
            }
            return file;
            });

            this.fileList.value = resFileList;
        },

        onFinish: function() {
            if (this.fileList[0] != null) {
                console.log(this.fileList[0])
                BaseRequest.post('products/product-create/', {
                    name: this.product.name,
                    description: this.product.description,
                    price: this.product.price,
                    image: this.fileList[0].thumbUrl,
                    category: this.value_category.value,
                    brand: this.value_brand.value,
                })
                .then(response => {
                        this.errors = {}
                        this.createSuccessNotification()
                        this.$router.push({ name: 'product.list'});
                    }
                )
                .catch(error=> {
                    this.errors = error.response.data
                    console.log(this.errors)
                });
            }
            
        },
        createSuccessNotification: function() {
            notification['success']({
                message: 'Create successfully!',
                description:
                'Product was create! ',
            });
        }
    }
})
</script>