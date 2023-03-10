<template>
	<view>
		<uni-section title="个人信息" type="line"></uni-section>
				<uni-list>
					<uni-list-item title="姓名" :rightText="user1.name" />
					<uni-list-item title="学号" :rightText="user1.student_number" />
					<uni-list-item title="电话" :rightText="user1.number" />
					<uni-list-item title="是否可用" :rightText="user1.illegal_number >15?'不可用':'可用'" />
				</uni-list>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				user1:{},
			}
		},
		onLoad() {
			var that=this;
			uni.request({
				url:getApp().globalData.urlRoot+"user/loadInfo",
				header: {'Authorization':getApp().globalData.token,
				   'content-type':'application/x-www-form-urlencoded'},
				data:{
						"id":getApp().globalData.uid,
					},
				method:"POST",
				success: (res) => {
					if (res.data.suc) {
						that.user1=res.data.user
					}else{
						console.log("上传失败")
						uni.showToast({
							title: String(res.data.message),
							icon: 'checkmarkempty'
						})
					}
				},
			})
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
