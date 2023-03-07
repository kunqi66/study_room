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
		<view class="temp">
			<view class="notice_home">
					<uni-title type="h1" title="公告" color="#ffaaa7"></uni-title>
			</view>
			<view class="weather_home" @click="createWeather()">
				<view>
				<uni-icons type="contact" size="18"></uni-icons>
				天气：{{ realWeather.info }}
				</view>
				<view>
				<uni-icons type="fire" size="18"></uni-icons>
				温度：{{ realWeather.temperature}} 
				</view>
				<view>
				<uni-icons type="contact" size="18"></uni-icons>
				风向：{{ realWeather.direct }} 
				</view>   
				<view>
				<uni-icons type="contact" size="18"></uni-icons>
				风力：{{ realWeather.power }}
				</view>
			</view> 
			<view class="manage_home" @click="open()">
				
				<uni-list >
					<uni-list-item title="自习室规定"></uni-list-item>
					<uni-list-item title="第一条通知" note="0.0"></uni-list-item>
					<uni-list-item title="第二条通知" note="0.0"></uni-list-item>
					
				</uni-list>
					
			</view> 
			<view class="complaint_home">
				投诉写这里
			</view>  

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
		  <uni-list-item title="5555555555555555555555" note="0.0"></uni-list-item>
		  <uni-list-item title="555" note="0.0"></uni-list-item>
		 <uni-list-item title="555" note="0.0"></uni-list-item>
		 <uni-list-item title="555" note="0.0"></uni-list-item>
		 <uni-list-item title="555" note="0.0"></uni-list-item>
		 <uni-list-item title="555" note="0.0"></uni-list-item>
		 <uni-list-item title="555" note="0.0"></uni-list-item>
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
				noticelist:[{
					"notice_title":"公告",
					"notice_text":"我看谁再给我卷",
					"notice_time":"2023年3月7日"
				},
				{
					"notice_title":"公告",
					"notice_text":"我看谁再给我卷",
					"notice_time":"2023年3月7日"
				},
				{
					"notice_title":"公告",
					"notice_text":"我看谁再给我卷",
					"notice_time":"2023年3月7日"
				},
				{
					"notice_title":"公告",
					"notice_text":"我看谁再给我卷",
					"notice_time":"2023年3月7日"
				},
				{
					"notice_title":"公告",
					"notice_text":"我看谁再给我卷",
					"notice_time":"2023年3月7日"
				},
				{
					"notice_title":"公告",
					"notice_text":"我看谁再给我卷",
					"notice_time":"2023年3月7日"
				}],
				
			}
			},
		onLoad() {
			this.loadWeather()
			console.log("获取到当前的天气"+this.realWeather+"获取数据"+this.weather)
		},
		methods: {
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
			}
	
		}
	}
</script>

<style>
	.tanchuang1{
		background-color: azure;
		width: 300px;
		height: 550px;
		border-radius: 10px;
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
		width: 45%;
		margin-left: 5%;
		font-size: 18px;
		height: 120px;
		float: left;
	}
	.notice_home{
		width: 90%;
		margin-left: 5%;
		/* background-color: black; */
		margin-bottom: 20px;
	}
	.manage_home{
		background-color: bisque;
		height: 120px;
		width: 45%;
		margin-right: 5%;
		float: right;
	}
	.complaint_home{
		margin-top: 20px;
	}
	
</style>
