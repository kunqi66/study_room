<template>
	<view>
		<uni-section title="编辑公告:" type="line"></uni-section>
			<view class="example-body">
				<uni-easyinput  type="textarea" v-model="formData.text" placeholder="请输入新增规定">
				</uni-easyinput>
			</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				formData:{},
			}
		},
		methods: {
		},
	}
</script>

<style>
page{
	margin-left: 15px;
	margin-right: 15px;
}
</style>
