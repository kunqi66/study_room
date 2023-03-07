<template>
	<view>
		<view style="height: 150px;">
			<button style="background-color:#eef7fe; border: none; size:auto;">
				<view class="image_home">
					<image class="avatar" v-if="managerview == -1" src="/static/logo.png" />
					<image class="avatar" v-if="managerview != -1" src="/static/l.jpg"></image>
					<view>
						<span style="text-align: center;size: 50px;" >
						<text v-if="managerview == -1" class="img-text">用户昵称</text>
						<text v-if="managerview != -1" class="img-text">{{ userInfo.name }}</text>
						</span>
					</view>
				</view>
			</button>
		</view>
		<view class="list_home">
		<uni-list style=" border-radius: 18rpx;">
			<view style="border-radius: 18rpx;" v-for="(item,index) in List">
			<uni-list-item :title="item.title" link :to="item.url" @click="onClick($event,1)" ></uni-list-item>
			</view>
			
		</uni-list>
		</view>
		<view style="width: 80%; margin-left: 10%; margin-top: 70px;">
			<button  v-if="managerview == -1"  type="primary" @click="wx_login()" >用户一键微信登录</button>
		</view>
		
		<view style="width: 80%; margin-left: 10%; margin-top: 15px;">
			<button  v-if="managerview == -1"  type="primary" @click="mana_login()" >管理员身份认证</button>
		</view>
		
		<view style="width: 80%; margin-left: 10%; margin-top: 50px;">
			<button  v-if="managerview != -1" type="warn" plain="true" @click="user_logout()" >退出登录</button>
		</view>
		
		
		
		
		<uni-popup ref="register" type="center" border-radius="14" width="1000rpx" height="6000px" >
			<view style="margin: 50px;">
					<!-- Card start -->
					<uni-card>
						<uni-title type="h1" align="center" title="填写个人信息"></uni-title>
							<uni-forms :model-value="registerForm">
								<uni-forms-item label="姓名">
									<uni-easyinput type="text" v-model="registerForm.name" placeholder="请输入姓名" />
								</uni-forms-item>
								<uni-forms-item label="学号">
									<uni-easyinput type="text" v-model="registerForm.student_number" placeholder="请输入您的学号" />
								</uni-forms-item>
								<uni-forms-item label="电话">
									<uni-easyinput type="text" v-model="registerForm.number" placeholder="请输入您的电话" />
								</uni-forms-item>
							</uni-forms>
						<view slot="actions" class="card-actions">
							<view class="card-actions-item2">
								<button style="width: 50%;" type="primary" size="mini" @click="submitRegister()">提交</button>
								<button style="width: 50%;" type="primary" size="mini" @click="closeRegister()">关闭</button>
							</view>
						</view>
					</uni-card>
			</view>
		</uni-popup>
		
		
		
	</view>
</template>

<script>
	export default{
		data() {
			return {
				logFlag: false,
				openid :'',
				managerview:getApp().globalData.uid,
				paswdshow: false,
				register: false,
				registerForm:{},
				resetForm:{},
				userInfo:{},
				List:[{
					title:"个人信息",
					url:"",
				},{
					title:"修改个人信息",
					url:"",
				},
				{
					title:"预约自习室记录",
					url:"",
				},{
					title:"个人违规记录",
					url:"",
				}]
			}
		},
		methods:{
			mana_login(){
				uni.request({
					url:"http://apis.juhe.cn/simpleWeather/query",
					header: {'content-type':'application/x-www-form-urlencoded'},
					method:"GET",
					data:{
						"city":"太原",
						"key":"66b934d1e96ee28fcff59c901dc97a21",
					},
					success(res) {
						console.log(res);
					}
				})
			},
			user_logout(){
				var that=this;
				this.managerview=-1,
				getApp().globalData.uid=-1
			},
			submitRegister(){
				var that=this;
				uni.request({
					url:getApp().globalData.urlRoot+"user/register",
					header: {'Authorization':"wutoken",
								'content-type':'application/x-www-form-urlencoded'},
					method: "POST",
					data:{
						"name": that.registerForm.name,
						"student_number":that.registerForm.student_number,
						"number":that.registerForm.number,
						"oid":that.openid
					},
					success(res) {
						if(res.data.suc){
							console.log("注册成功");
							uni.showToast({
								title: "信息绑定成功！",
								icon: 'checkmarkempty'
							})
							that.$refs.register.close()
						}
					}
				})
			},
			closeRegister(){
				this.$refs.register.close()
			},
			wx_login(){
				var that =this;
				 let wxspAppid = 'wxe73f973f5099f105';
				 let wxspSecret = '07ff2880db69db6936266d1cfa2439ca';
				 let oid= '';
				 uni.login({
				 	provider:'weixin',
				       success(res) {
						uni.getUserInfo({
							provider:'weixin',
							success:function(infoRes){
					   	    that.userInfo = infoRes.userInfo
					    	console.log(that.userInfo)
							}
						});
				         if (res.code) {
				           //发起网络请求
				           uni.request({
				           //这里填你自己的appid 和 wxspSecret
				             url: "https://api.weixin.qq.com/sns/jscode2session?appid=" + wxspAppid+"&secret=" + wxspSecret + "&js_code=" + res.code + "&grant_type=authorization_code" ,
				             method: "POST",
				             success(res){
				 				oid=res.data.openid
				 				that.openid=oid
								console.log(that.openid)
				 				uni.request({
				 					header: {'Authorization':"wutoken",
				 								'content-type':'application/x-www-form-urlencoded'},
				 					url: getApp().globalData.urlRoot + "user/Login",
				 					data:{
				 						"oid" :oid,
				 					},
				 					method:"POST",
				 					success: (res1) => {
				 						if(res1.data.suc){
											getApp().globalData.uid=res1.data.uid;
											that.managerview=res1.data.uid;
											console.log("id为"+getApp().globalData.uid)
											that.userInfo.name=res1.data.name
											console.log(res1)
											console.log(that.userInfo.name)
											uni.showToast({
												title: "登录成功！",
												icon: 'checkmarkempty'
											})
										}else{
											uni.showToast({
												title: "首次登录请绑定信息",
											})
											that.$refs.register.open()
										}
				 					}
				 				})
				 			},
				             fail(data){}
				           })
				         } else {console.log('登录失败！' + res.errMsg)}
				       }
				})
			}
		}
	}
</script>

<style>
	button::after{
		  border: none;
		}
		page{
			background-color: #eef7fe;
		}
		.login_button{
				width: 200rpx;
				height: 50rpx;
				display: flex;
				margin-top: 30rpx;
				line-height: 50rpx;
				justify-content: center;
				border-radius: 25px;
				border: 3rpx solid #6699FF;
				font-size: 28rpx;
			}
		.bg-click {
				top: 3upx;
				background-color: #a7a9ff;
			}
		.content {
			background-image: "/static/980.webp";
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
		}
	
		.logo {
			height: 200rpx;
			width: 200rpx;
			margin-top: 200rpx;
			margin-left: auto;
			margin-right: auto;
			margin-bottom: 50rpx;
		}
	
		.text-area {
			display: flex;
			justify-content: center;
		}
	
		.title {
			font-size: 36rpx;
			color: hsl(30, 100%, 50%);
		}
		
		//圆形头像
		.avatar{
		    width: 150upx;
		    height: 150upx;
		    border-radius: 50%;
		    // transform: translateY(-50%);
		    margin-top: -75upx;
		}
		.image_home{
			margin-top: 50px;
			margin-left: 20px;
		}
		.img-text{
			padding: 0 10upx;
			color: dimgrey;
			font-size: 20px;
		}
		
		.list_home{
			margin-top: 30px;
	/* 圆角 */
		  border-radius: 80rpx;
		
		  /* 边 */
		  border: 1rpx solid #E0E3DA;
		  /* 阴影 */
		  box-shadow:2rpx 6rpx 0rpx #e5e8df;
	
			height: auto;
			width: 90%; 
			text-align: center;
			margin-left: 5%;
		}
</style>