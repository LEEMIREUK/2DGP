# 2DGP 기말 프로젝트
-----------------------------------
### 1. 게임 소개
>+ 게임 제목: 1997
>+ 1997은 오락실게임 1945의 모작입니다.
>+ 제가 1997년생이여서 게임이름을 1945가 아닌 1997로 지었습니다.
>####      [Screenshots]
>![1945](https://user-images.githubusercontent.com/32861131/94073717-e4488800-fe32-11ea-93d5-09b78c45a9ba.png)
>+ 게임 소개: 비행기를 조종하여 적군을 쓰러뜨리는 게임입니다.
>  타이틀 화면에서 비행기 선택하는 화면으로 넘어가며 비행기를 선택한 후에 게임이 진행됩니다.
>  총알은 무제한이며 아이템을 먹으면 점점 총알이 업그레이드 됩니다.
>  죽으면 총알의 업그레이드는 리셋되며 목숨하나가 차감됩니다.
### 2. GameState
>+ GameState는 크게 4가지이며 이름은 아래와 같습니다.
>```
>TitleState
>MainState
>GameState
>Option
>```
### 3. 각 GameState별 다음 항목
>+ TitleState
>   + 게임 시작 전 타이틀 화면을 보여주는 State입니다.
>   + 객체 목록: title_image
>   + 2초 후 change_state를 이용해 MainState로 이동합니다.  
>+ MainState
>   + 타이틀 화면 다음으로 나오는 화면이며 게임시작, 설정, 게임종료 등을 설정할 수 있는 화면입니다.
>   + 객체 목록: Main_image
>   + 게임시작을 누르면 change_state를 통해 GameState로 이동합니다.
>   + ↑ ↓ 키를 이용하여 메뉴를 선택할 수 있습니다.
>   + 설정을 누르면 push_state로 Option창을 띄워줍니다.
>   + 게임종료를 누르면 종료됩니다.
>+ GameState
>   + 본격적으로 게임 플레이를 보여주는 화면입니다.
>   + 객체 목록: Player, Enemy, Bullet(Player, Enemy), Item 등
>   + Event를 통해 Player는 ↑ ↓ ← → 키로 이동이 가능하며 Left_ctrl 키로 총알을 발사할 수 있고 Left_shift 키로 스킬을 사용할 수 있습니다.  
>   + Enemy는 랜덤으로 생성되며 움직이는 패턴을 구현합니다. 적의 이동을 예측할 수 없도록 움직임을 구현합니다.
>   + Item은 일정 시간이 지나면 필드에 나타나며 먹으면 Player에게 좋은 효과를 줍니다.
>   + ESC 키를 눌러 Option 창으로 push_state 됩니다.
>+ Option
>   + 옵션창을 띄워주는 State입니다.
>   + MainState에서 옵션창을 열 경우 이전 화면, 게임 설정을 할 수 있습니다.
>   + GameState에서 옵션창을 열 경우 이전 화면, 게임 재시작, 게임 설정, 게임 종료를 할 수 있습니다.
>   + ↑ ↓ 키를 이용하여 목록을 선택할 수 있습니다.
>   + 옵션창은 push_state를 이용합니다.
>#####      [State 구조]  
>![State](https://user-images.githubusercontent.com/32861131/94073721-e6124b80-fe32-11ea-9562-ab827f40a2df.PNG)
### 4. 필요한 기술
>+ 많은 객체를 생성하고 사용해야 하기 때문에 클래스를 잘 다루는 기술이 필요합니다.
>+ 이 게임의 핵심은 충돌처리이기 때문에 앞으로 수업 이후에 충돌처리에 관해 배우면 좋을 것 같습니다.

### 개발 내용
>![개발내용](https://user-images.githubusercontent.com/32861131/95718825-ee2f0f80-0ca9-11eb-8636-3cc9e9967248.PNG)

### 개발 일정
>![개발일정](https://user-images.githubusercontent.com/32861131/95719363-a9f03f00-0caa-11eb-9181-511f198a6b2f.PNG)
>#####  개발일정은 10월 12일에 시작하는 주를 1주차로 한다.
-----------------------------------
### 이미지 리소스 정보
>**resource information(pixel)**
>
>player1 : 23 x 31  
>player1_animation : 161 x 31 - 1frame 23 x 31  (x 7)  
>player1_start_animation : 230 x 117 - 1frame 23 x 117 (x 10)  
>player1_explosion : 448 x 32 - 1frame  32 x 32 (x 14)  
>player1_select : 240 x 460  
>player1_select_onclick : 240 x 460  
>player1_bullet1 : 45 x 34 - 1frame 15 x 34  
>player1_bullet2 : 45 x 34 - 1frame 50 x 60  
>player1_loading : 224 x 320  
>
>player2 : 21 x 31  
>player2_animation : 147 x 31 - 1frame 21 x 31 (x 7)  
>player2_start_animation : 231 x 109 - 1frame 21 x 109 (x 11)  
>player2_explosion : 384 x 32 - 1frame 32 x 32 (x 12)  
>player2_select : 240 x 460  
>player2_select_onclick : 240 x 460  
>player2_bullet1 : 45 x 30 - 1frame 15 x 30  
>player2_bullet2 : 45 x 30 - 1frame 50 x 60  
>player2_loading : 224 x 321  
>
>enemy : 96 x 32 - 1frame 32 x 32 (x 3)  
>enemy_bullet : 10 x 10  
>enemy_explosion  : 192 x 32 - 1frame 32 x 32 (x 6)  
>
>razer_skill : 528 x 869 - 1frame 33 x 869 (x 16)  
>fire_skill : 584 x 122 - 1frame 73 x 122 (x 8)  
>
>stage_map : 800 x 7000  
>title : 300 x 300  
>main_image : 4480 x 320 - 1frame 224 x 320 (x 20)  
>fighter_animation1 : 471 x 1290 - 1frame 157 x 86 (x 45)  
>start_image : 1730 x 142 - 1frame 346 x 142 (x 3)  
>exit_image : 1265 x 142 - 1frame 253 x 142 (x 5)  
>button_image : 30 x 15 - 1frame 15 x 15 (x 2)  
>item_image : 120 x 13 - 1frame 20 x 13 (x 6)  
-----------------------------------
### 중간 발표 자료
>진행상황   
>![진행상황](https://user-images.githubusercontent.com/32861131/99875908-7358fd00-2c36-11eb-9110-220a64274470.PNG)   
>git commit 횟수   
>![커밋횟수](https://user-images.githubusercontent.com/32861131/99875902-6dfbb280-2c36-11eb-9ed6-3c551dab385b.PNG)   
>변경내용   
>![변경내용](https://user-images.githubusercontent.com/32861131/99875906-718f3980-2c36-11eb-95de-6b05fd9a104c.PNG)   
>상호작용   
>![상호작용](https://user-images.githubusercontent.com/32861131/99875911-7653ed80-2c36-11eb-9283-94a64c7c7565.PNG)   
>class 구성   
>![class 구성](https://user-images.githubusercontent.com/32861131/99875910-748a2a00-2c36-11eb-9881-5f6e430be717.PNG)   
>가장 중요한 클래스   
>```
>class Player:
>class Enemy:
>```
>플레이어 클래스에는 def init, def draw, def update, def fire, def skill, def explosion 함수가 있습니다.   
>이 클래스는 stage.py에서 생성됩니다.   
>
>적군 클래스에는 def init, def draw, def update, def fire, def explosion 함수가 있습니다.   
>이 클래스는 stage.py에서 일정 시간마다 생성됩니다.   
>적군은 생성되는 순간 플레이어의 위치값을 받아와 그 위치를 향해 움직입니다.   
>적군은 일정 간격으로 총알을 발사하며 그 순간의 플레이어의 위치값을 받아와 그 위치를 향해 총알을 발사합니다.   
