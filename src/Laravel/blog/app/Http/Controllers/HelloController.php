<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\DB;
use App\Http\Requests\HelloRequest;
use Validator;

use Illuminate\Support\Facades\Log;
use App\Models\Image;
use App\Models\News;

global $head, $style, $body, $end;
$head = '<html><head>';
$style = <<<EOR
<style>
body {font-size:16pt; color:#999;}
h1 { font-size:100pt; text-align:right; color:#eee;
    margin:40px 0px -50px 0px; }
</style>
EOR;
$body = '</head><body>';
$end = '</body></html>';

function tag($tag, $txt) {
    return "<{$tag}>" . $txt . "</{$tag}>";
}

class HelloController extends Controller
{
    public function index(Request $request)
    {
        $image = DB::select('select * from news');
        $items = DB::select('select * from news');
        return view('index', ['items' => $items, 'image' => $image]);
    }
    public function upload(Request $request)
    {
        // ディレクトリ名
        $dir = 'sample';

        // アップロードされたファイル名を取得
        $file_name = $request->file('image')->getClientOriginalName();

        // 取得したファイル名で保存
        $request->file('image')->storeAs('public/' . $dir, $file_name);

        // ファイル情報をDBに保存
        $image = new Image();
        $image->name = $file_name;
        $image->path = 'storage/' . $dir . '/' . $file_name;
        $image->save();

        return redirect('/hello');
    }
    public function post(Request $request)
    {
        $items = DB::select('select * from people');
        return view('index', ['items' => $items]);
    }

    public function add(Request $request)
    {
        return view('hello.add');
    }

    public function create(Request $request)
    {
        // ディレクトリ名
        $dir = 'sample';

        // アップロードされたファイル名を取得
        $file_name = $request->file('image')->getClientOriginalName();

        // 取得したファイル名で保存
        $request->file('image')->storeAs('public/' . $dir, $file_name);

        // ファイル情報をDBに保存
        $image = new News();
        $image->title = $request->title;
        $image->message = $request->message;
        $image->image_name = $file_name;
        $image->image_path = 'storage/' . $dir . '/' . $file_name;
        $image->save();

        // $param = [
        //     'title' => $request->title,
        //     'image_path' => $request->image_path,
        //     'image_name' => $request->image_name,
        //     'message' => $request->message,
        // ];
        // DB::insert('INSERT INTO news (title,image_path,image_name,message) VALUES (:title,:image_path,:image_name,:message)',$param);
        $items = DB::select('select * from news');
        return redirect('/hello', ['items' => $items]);
    }


    public function edit(Request $request)
    {
        $param = ['id' => $request->id];
        $item = DB::select('SELECT * FROM people where id = :id',$param);
        return view('hello.edit',['form'=>$item[0]]);
    }

    public function update(Request $request)
    {
        $param = [
            'id' => $request->id,
            'name' => $request->name,
            'mail' => $request->mail,
            'age' => $request->age,
        ];
        DB::update('UPDATE people SET name = :name,mail = :mail,age = :age where id = :id',$param);
        return redirect('hello');
    }

    public function del(Request $request)
    {
        $param = [
            'id' => $request->id
        ];
        $item = DB::select('SELECT * FROM people WHERE id = :id',$param);
        return view('hello.del',['form'=>$item[0]]);
    }

    public function remove(Request $request)
    {
        $param = ['id'=>$request->id];
        DB::delete('DELETE FROM people where id = :id',$param);
        return redirect('hello');
    }

    // public function index(Request $request)
    // {
    //     return view('index', ['data'=>$request->data]);
    // }
    // public function index()
    // {
    //     $data = [
    //         'msg'=>'',
    //     ];
    //     return view('index', $data);
    // }
    // public function index()
    // {
    //     // $data = [
    //     //     ['name'=>'山田たろう', 'mail'=>'taro@yamada'],
    //     //     ['name'=>'田中はなこ', 'mail'=>'hanako@flower'],
    //     //     ['name'=>'鈴木さちこ', 'mail'=>'sachico@happy'],
    //     // ];
    //     // return view('index', ['data'=>$data]);
    //     return view('index', ['message'=>'Hello!']);
    // }
    // public function post(Request $request)
    // {
    //     $data = [
    //         'msg'=>$request->msg,
    //     ];
    //     return view('index', $data);
    // }
    // public function index() {
    //     global $head, $style, $body, $end;

    //     $html = $head . tag('title','Hello/Index') . $style . $body
    //         . tag('h1','Index') . tag('p','this is Index page')
    //         . '<a href="/hello/other">go to Other page</a>'
    //         . $end;
    //     return $html;
    // }

    // public function other() {
    //     global $head, $style, $body, $end;

    //     $html = $head . tag('title','Hello/Index') . $style . $body
    //         . tag('h1','Other') . tag('p','this is Other page')
    //         . $end;
    //     return $html;
    // }

    // public function __invoke() {
    //     return <<<EOR
    //     <html>
    //     <head>
    //     <title>Hello</title>
    //     <style>
    //     body {font-size:16pt; color:#999;}
    //     h1 { font-size:100pt; text-align:right; color:#eee;
    //         margin:40px 0px -50px 0px; }
    //     </style>
    //     </head>
    //     <body>
    //         <h1>Singel Action</h1>
    //         <p>これは、シングルアクションコントローラのアクションです。</p>
    //     </body>
    //     </html>
    //     EOR;
    // }
}
// class HelloController extends Controller
// {
//     public function index($id='noname', $pass='unkown'){
//         return <<<EOR
// <html>
// <head>
// <title>Hello/Index</title>
// <style>
// body {font-size:16pt; color:#999;}
// h1 { font-size:100pt; text-align:right; color:#eee;
//     margin:40px 0px -50px 0px; }
// </style>
// </head>
// <body>
//     <h1>Index</h1>
//     <p>これは、Helloコントローラのindexアクションです。</p>
//     <ul>
//         <li>ID: {$id}</li>
//         <li>PASS: {$pass}</li>
//     </ul>
// </body>
// </html>
// EOR;
//     }
// }
