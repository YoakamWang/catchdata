from MyQR import myqr

def main():
    myqr.run(
        words="https://www.ef.com.cn/",
        picture='qr.gif',
        colorized=True,
        save_name='Animated.gif'
    )
if __name__=="__main__":
    main()
