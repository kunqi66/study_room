<template>
	<view>
		<uni-section title="日期:" type="line"></uni-section>
				<view class="example-body">
					<uni-datetime-picker type="date" :clear-icon="false" v-model="formData.date" @maskClick="maskClick" />
				</view>
		<uni-section title="公告题目:" type="line"></uni-section>
			<view class="example-body">
				<uni-easyinput  type="text" v-model="formData.text" placeholder="请输入公告标题">
				</uni-easyinput>
			</view>
		<uni-section title="公告内容:" type="line"></uni-section>
			<view class="example-body">
				<uni-easyinput  type="textarea" v-model="formData.text" placeholder="请输入公告内容">
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
					url:getApp().globalData.urlRoot+"manager/submitNotice",
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					data:{
							"title": that.formData.title,
							"text": that.formData.text,
							"date": that.formData.date,
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
