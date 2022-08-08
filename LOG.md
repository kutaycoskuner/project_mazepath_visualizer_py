# Log
`Started 31-May-2020`

# Todo
- [x] 31-May-2022 implement core algorithm
- [x] 31-May-2022 set up git repository
- [x] 31-May-2022 data driven input
    - [x] 31-May-2022 add command line option to specify sleep timer. ex: -sleep 0.3
    - [x] 31-May-2022 add command line option to speify maze layout via text file -in ".data/maze1.txt" 
    - [x] 31-May-2022 add clo to specify search strategy. ex: -dfs, -bfs
    - [x] 09-Jun-2022 31-May-2022 add clo color option. ex: -color_maze blue -color_path red
    - [x] 09-Jul-2022 add command line gui option
    - 08-Aug-2022 validate input
    - 08-Aug-2022 gui send package optimization
- [p] 09-Jul-2022 31-May-2022 search the web for python gui lib and find one that supports pixel plotting for drawing the maze
    - [x] 12-Jun-2022 add: gui basic layout
    - [x] 09-Jul-2022 tkinter: text: print in color | print in pixel
    - [x] 19-Jul-2022 button functions and 
    - [x] 19-Jul-2022 add son halde rengi degistir
    - [x] 09-Aug-2022 19-Jul-2022 browse button select file
    - 10-Jun-2022 chg: stylize gui: https://www.youtube.com/watch?v=axMG3fkIhO4
    - 09-Jul-2022 size/animation sliders
    - 19-Jul-2022 playing animation on time
    - 19-Jul-2022 add: kullaniciya maze yazdirma opsiyonu
- [x] 09-Jul-2022 07-Jul-2022 upg: color ifleri map e cevir
- [x] 09-Jul-2022 12-06-2022 arch model-view-controller architecture implementation 
- [x] 17-Jul-2022 gui ye path aktarma -> pass copy/reference, debugger algoritma problem, path silme
- 31-May-2022 fix broken mazes or defense
- 05-Jun-2022 fix py main.py -t .3 -d "data/maze0.txt" -df | data belirtilmesine ragmen df girildiginde verilen maze i gormezden geliyor.
- 07-Jul-2022 org: vsc hizlandir kod navigasyonu
- 09-Jul-2022 org: documentation yaz
    - [x] 07-Aug-2022 documentation outline
- 13-Jul-2022 add: farkli dille calisabilen view? electron?
- 09-Aug-2022 fix: bir maze import edip ustune yenisini import edince bir oncekini silmiyor

# Problems
- tkinter: grid kullaninca objeleri saga yaslayamiyorum.
- tkinter: pack kullaninca margin veremiyorum.

# Keys - Discretized Actions 1.2
- org: organization, decisions, notebook changes
- arch: architectural, framework change, tryout

- com: compatibility update
- add: add, insert, data content

- del: deleted
- fix: fix a bug or problem
- upg: update, upgraded, progressed, optimize
- chg: stylistic change

- std: study, learn, test
- wip: work in progress
- mix: multiple additions

# Push procedure 1.3
- add log
- check todo
- change time log
- push

# LOG
- 09-Aug-2022 0.15      add: gui browse button
- 07-Aug-2022 0.14.10   wip: readme documentation outliner
- 19-Jul-2022 0.14.9    wip: changing color of gui at solution step
- 19-Jul-2022 0.14.8    wip: gui-logic interaction, working buttons;
- 09-Jul-2022 0.14.7    wip: cla gui 02.11; pixel output with canvas 03.10;
- 09-Jul-2022 0.14.6    wip: controller in icinde kalan model parcasini model e aktardim 00.28; 
- 07-Jul-2022 0.14.5    wip: controller/model i guisiz calistirma
- 03-Jul-2022 0.14.4    wip: view elemanlari view icinde olusturuldu.
- 24-Jun-2022 0.14.3    wip: view class ini implement etmeye calisiyorum.
- 12-Jun-2022 0.14.2    wip: gui arch problem: gui-logic communication 
- 10-Jun-2022 0.14.1    wip: gui learning: widgets: frames, buttons, labels
- 09-Jun-2022 0.14      add: command line argument: opt red/green/blue color selection for obstacle and path
- 31-May-2022 0.13      add: command line argument: opt select search algorithm df|bf
- 31-May-2022 0.12      add: command line argument: opt data path
- 31-May-2022 0.11      add: command line argument: opt time delay
- 31-May-2022 0.10      std: maze solver first implementation s: tech with tim, 2022, 3 mini python projects - for intermediates