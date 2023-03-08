<template>
			<view class="content">
				<view style="margin:100px;"></view>
				<view class="text_home">
					<uni-forms>
						<uni-forms-item label="邮箱" name="email">
							<uni-easyinput v-model="userInfo.account" type="text" placeholder="请输入用户名" />
						</uni-forms-item>
						<uni-forms-item label="邮箱" name="password">
							<uni-easyinput  v-model="userInfo.password" type="password" placeholder="请输入密码" />
						</uni-forms-item>
					</uni-forms>
				</view>
				<view class="button_home">
					<button type="primary"   @click="login()">认证</button>
				</view>
				
			</view>
</template>

<script>
	export default {
		data() {
			return {
				userInfo :{},
			}
		},
		methods: {
			login(){
				
				uni.navigateTo({
					url:"/pages/manager/home",
				})    //调试用
				
				var that=this;
				uni.request({
					header: {'Authorization':getApp().globalData.token,
					   'content-type':'application/x-www-form-urlencoded'},
					url:getApp().globalData.urlRoot+"manager/Login",
					data:{
						"account": that.userInfo.account,
						"password": that.userInfo.password,
					},       //json
					method:"POST",
					success: (res) => {
						if(res.data.suc){
							console.log(res.data.message)
							uni.showToast({
								title: "登录成功！",
								icon: 'checkmarkempty'
							})
							uni.navigateTo({
								url:"/pages/manager/home",
							})
						}else{
							console.log(res.data.message)
							uni.showToast({
								title: String(res.data.message),
								icon: 'closeempty'
							})
						}
					},
					fail() {
						uni.showToast({
							title: "登录失败！",
							icon: 'closeempty'
						})
						console.log("登陆失败")
					},
					
				})
			},
		}
	}
</script>
<style lang="scss">
	page{
		background-color: #eef7fe;
	}
	.text-home{
		padding-top: 100px;
		margin-top: 100px;
		justify-content: center;
		width: 90%;
	}
	.button_home{
		width: 75%;
	}
	.content {
		background-image: "/static/980.webp";
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
</style>
