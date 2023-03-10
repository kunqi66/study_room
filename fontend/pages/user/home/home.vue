<template>
	<view>
		<view class="title">
			公告
		</view>
		<view class="notice_home" @click="tanchuang">
				<view class="notice_title">
					{{noticelist[0].notice_title}} 
				</view>
				<view class="notice_text">
					{{noticelist[0].notice_text}}
				</view>
				<view class="notice_time">
					{{noticelist[0].notice_time}}
				</view>
		</view>
		<view>
			<div class="showImg" >
			   
			    <img @mouseover="changeInterval(true)" 
			         @mouseleave="changeInterval(false)"  
			         v-for="(item) in imgArr" 
			         :key="item.id"
			         :src="item.url" 
			         alt="暂无图片" 
			         v-show="item.id===currentIndex" 
			         >
			    
			    <div  @click="clickIcon('up')"   class="iconDiv icon-left"> 
			        <i class="el-icon-caret-left"></i>
			    </div>
			  
			    <div  @click="clickIcon('down')"  class="iconDiv icon-right">
			        <i class="el-icon-caret-right"></i>
			    </div>
			  
			    <div class="banner-circle">
			        <ul>
			            <li @click="changeImg(item.id)" 
			                v-for="(item) in imgArr" 
			                :key="item.id"
			                :class="item.id===currentIndex? 'active': '' "
			             ></li>
			        </ul>
			    </div>
			</div>

		</view>
		
		
		<view class="temp">
			<view class="weather_home" @click="createWeather()">
				<view>
				<uni-icons type="contact" size="18"></uni-icons>
				天气：{{ realWeather.info }}
				 &nbsp;
				<uni-icons type="fire" size="18"></uni-icons>
				温度：{{ realWeather.temperature}} 
				</view>
				<view>
				<uni-icons type="contact" size="18"></uni-icons>
				风向：{{ realWeather.direct }}
				&nbsp;
				<uni-icons type="contact" size="18"></uni-icons>
				风力：{{ realWeather.power }}
				</view>
			</view> 
			

		</view>
		<view class="manage_home" @click="open()">
			
			<uni-list-item title="1.手机调至静音模式，接听电话请到室外接听。" note="0.0"></uni-list-item>
			 <uni-list-item title="2.请保持安静，如需看视频，请戴上耳机。" note="0.0"></uni-list-item>
			<uni-list-item title="3.请勿在学习区域吃东西。" note="0.0"></uni-list-item>
				
		</view> 
		<view class="feedback">
						<button style="width: 50%;" type="primary" plain="true" @click="goto('/pages/u')">投诉点这里哦</button>
					</view>
		
			<uni-popup ref="weather" type="center" background-color="" border-radius="14">
				<view class="tanchuang1">
					<view v-for="(item,index) in weatherList">
						<uni-section :title="item.date" type="line"></uni-section>
						<view>风向:{{item.direct}}</view>
						<view>温度:{{item.temperature}}</view>
						<view>天气:{{item.weather}}</view>
					</view>
				</view>
			</uni-popup> 

		
		   
		  <uni-popup ref="guiding" type="center"  >
			<view style="">
				  <uni-list-item title="1.手机调至静音模式，接听电话请到室外接听。" note="0.0"></uni-list-item>
				  <uni-list-item title="2.请保持安静，如需看视频，请戴上耳机。" note="0.0"></uni-list-item>
				 <uni-list-item title="3.请勿在学习区域吃东西。" note="0.0"></uni-list-item>
				 <uni-list-item title="4.如需使用电脑，请使用静音键盘、鼠标。" note="0.0"></uni-list-item>
				 <uni-list-item title="5.轻声关门，整理东西、起身落座、翻书时，请尽量降低声音。" note="0.0"></uni-list-item>
				 <uni-list-item title="6.如有结伴同行的小伙伴需要讨论问题，可以到休息区或就餐区小声讨论" note="0.0"></uni-list-item>

			  </view>
			  
			  
			
						
		
		  </uni-popup>



			<uni-popup ref="notice_history" type="center">
				<view class="notice_tan">
					<view class="tanchuang2" v-for="(item,index) in noticelist">
							<view class="notice_title">
								{{noticelist[index].notice_title}} 
							</view>
							<view class="notice_text">
								{{noticelist[index].notice_text}}
							</view>
							<view class="notice_time">
								{{noticelist[index].notice_time}}
							</view>
					</view>
				</view>
			</uni-popup>
	</view>
</template>

<script>
	export default {
		
		
		data() {
			return {
				direct:"",
				weather:{},
				realWeather:{},
				weatherList:[
				],
				noticelist:[],
				currentIndex :0,
				timer:null,
				imgArr:[
				{	id:0,
				 url:"/static/log/自习1.jpg",
				},{
				    id:1,
				url:"/static/log/自习2.jpg",
				},{
					id:2,
				url:"/static/log/自习3.jpg",
				},
				]
				
			}
			},
		onLoad() {
			this.loadWeather()
			this.loadNotice()
			console.log("获取到当前的天气"+this.realWeather+"获取数据"+this.weather)
		},
		methods: {
			loadNotice(){
				var that=this;
				uni.request({
						header: {'Authorization':getApp().globalData.token,
						   'content-type':'application/x-www-form-urlencoded'},
						url:getApp().globalData.urlRoot+"manager/loadNotice",
						method:'POST',
						data:{
						},
						success: (res) => {
							if(res.data.suc){
								console.log("获取管理员列表成功")
								that.noticelist=res.data.form
								console.log(that.noticelist[0].title)
								console.log(res.data.form)
							}else{
								console.log("未查询到数据")
								console.log(res.data.message)
							}
						},
						fail() {
							uni.showToast({
								title: "获取失败！",
								icon: 'none'
							})
						}
					})
			},
			createWeather(){
				this.$refs.weather.open()
			},
			tanchuang(){
				this.$refs.notice_history.open()
			},
			open(){
			     this.$refs.guiding.open()
			   },
			loadWeather(){
				var that=this;
				uni.request({
					url:"http://apis.juhe.cn/simpleWeather/query",
					header: {'content-type':'application/x-www-form-urlencoded'},
					method:"GET",
					data:{
						"city":"太原",
						"key":"67322f26b8ec4e7a2cc8738f1905e5ed",
					},
					success(res) {
						console.log(res);
						that.weather=res.data.result
						that.realWeather=res.data.result.realtime
						that.weatherList=res.data.result.future
						
					}
				})
			},
	
	      startInterval(){
	      				clearInterval(this.timer);
	      				this.timer = setInterval(()=>{
	      					this.currentIndex++;
	      					if(this.currentIndex > this.imgArr.length-1){
	      						this.currentIndex = 0
	      					}
	      				},3000)
	      			},
		 clickIcon(val){
		 				if(val==='down'){
		 					this.currentIndex++;
		 					if(this.currentIndex===this.imgArr.length){
		 						this.currentIndex = 0;
		 					}
		 				}else{
		 					
		 					if(this.currentIndex === 0){
		 						this.currentIndex = this.imgArr.length;
		 					}
		 					this.currentIndex--;
		 				}
		 			},
		 changeImg(index){
		 				this.currentIndex = index
		 			},
	     changeInterval(val){
	     				if(val){
	     					clearInterval(this.timer)
	     				}else{
	     					this.startInterval()
	     				}
	     			},
					goto(){
										uni.navigateTo({
										url:"/pages/user/home/feedback"
									})
								}
	     		},
				mounted(){
							this.startInterval()
						}
		
	}
</script>

<style>
	.temp{
		text-align: center;
	}
	.tanchuang1{
		background-color: azure;
		width: 200px;
		height: 600px;
		border-radius: 10px;
		margin-left: 5%;
	}
	.title{
		width: 100%;
		height: 50px;
		font-size: 30px;
		text-align: center;
		color: rebeccapurple;
	}
	.notice_tan{
		padding: 8px;
		width:300px;
		height: 500px;
		background-color: azure;
		border-radius: 10px;
	}
	.notice_title{
		font-size: 18px;
		font-weight: bold;
		border-left: 5px solid #ffaa00;
		padding-left: 10px;
	}
	.notice_text{
		font-size: 18px;
		color: black;
	}
	.notice_time{
		font-size: 18px;
		color: #00a2f3;
		text-align: right;
	}
	.tanchuang2{
		margin-top: 8px;
		width:300px;
		background-color: azure;
		border-bottom: 1px dashed #686800 ;
	}
	.weather_home{
		margin-top: 10px;
		width: 90%;
		margin-left: 5%;
		font-size: 18px;
		height: 120px;
	}
	.notice_home{
		width: 90%;
		margin-left: 5%;
		/* background-color: black; */
		margin-bottom: 20px;
	}
	.manage_home{
		height: 120px;
		width: 90%;
		margin-left: 5%;
	}
	.complaint_home{
		margin-top: 20px;
	}
	
	li {
		list-style-type: none;
	}
	.showImg{
		position: relative;
		width: 90%;
		height: 240px;
		margin-left: 5%;
		overflow: hidden;
	}
	.showImg img{
		width: 100%;
		height: 100%;
	}
	
	.iconDiv{
		position: absolute;
		top: 50%;
		transform: translateY(-50%);
		width: 7px;
		height: 7px;
		border: 1px solid #666;
		border-radius: 4px;
		background-color: rgba(125,125,125,.2);
		line-height: 7px;
		text-align: center;
		font-size: 4px;
		cursor: pointer;
	}
	.iconDiv:hover{
		background-color: white;
	}
	.icon-left{
		left: 10px;
	}
	.icon-right{
		right: 10px;
	}
	
	.banner-circle{
		position: absolute;
		bottom: 0;
		width: 100%;
		height: 20px;
	}
	.banner-circle ul{
		margin: 0 50px;
		height: 100%;
		text-align: right;
	}
	.banner-circle ul li{
		display: inline-block;
		width: 14px;
		height: 14px;
		margin: 0 5px;
		border-radius: 7px;
		background-color: rgba(125,125,125,.8);
		cursor: pointer;
	}
	.active{
		background-color: black !important; 
	}
	
	.feedback{
			height: 50%;
			margin-top: 50%;
			
			
		}
	
</style>

