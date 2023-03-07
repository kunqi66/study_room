<template>
	<view>
		<view class="temp">
			<view class="notice_home">
					<uni-title type="h1" title="公告" color="#ffaaa7"></uni-title>
			</view>
			<view class="weather_home">
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
			<view class="manage_home">
				自习室规定：daisikjaksjdlajdlkasjdlskajsakdjaslkdhalksdjlkadjsdfsdfsdfsdf
			</view> 
			<view class="complaint_home">
				投诉写这里
			</view>  
		</view>   
	</view>
</template>

<script>
	export default {
		data() {
			return {
				direct:"",
				weather:{},
				realWeather:{},
			}
		},
		onLoad() {
			this.loadWeather()
			console.log("获取到当前的天气"+this.realWeather+"获取数据"+this.weather)
		},
		methods: {
			loadWeather(){
				var that=this;
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
						that.weather=res.data.result
						that.realWeather=res.data.result.realtime
					}
				})
			}
		}
	}
</script>

<style>
	.weather_home{
		width: 45%;
		margin-left: 5%;
		font-size: 18px;
		height: 120px;
		float: left;
	}
	.notice_home{
		width: 90%;
		margin-left: 5%;
		background-color: black;
	}
	.manage_home{
		background-color: bisque;
		height: 120px;
		width: 45%;
		margin-right: 5%;
		float: right;
	}
</style>
