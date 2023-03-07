<template>
	<view>
		<uni-section title="公告题目:" type="line"></uni-section>
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
			submitForm(){
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"manager/submitMana",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
							"text": that.formData.text,
						},
					method:"POST",
					success: (res) => {
						if (res.data.suc) {
							console.log('正常返回')
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}else{
							console.log("上传失败")
							uni.showToast({
								title: String(res.data.message),
								icon: 'checkmarkempty'
							})
						}
					},
				})
			}
		}
	}
</script>

<style>
page{
	margin-left: 15px;
	margin-right: 15px;
}
</style>
