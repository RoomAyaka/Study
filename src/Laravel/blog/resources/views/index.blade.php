@extends('layouts.helloapp')

@section('title', 'Index')

@section('menubar')
    @parent
    インデックスページ
@endsection

@section('content')
    {{-- <table>
        <tr><th>Name</th><th>Mail</th><th>Age</th></tr>
        @foreach ($items as $item)
            <tr>
                <td>{{$item->name}}</td>
                <td>{{$item->mail}}</td>
                <td>{{$item->age}}</td>
            </tr>
        @endforeach
    </table> --}}
    <table>
        <tr><th>Name</th><th>Mail</th><th>Age</th></tr>
        @foreach ($items as $item)

            <tr>
                <td>{{$item->title}}</td>
                <td><img src="{{ asset($item->image_path) }}"></td>
                <td>{{$item->image_name}}</td>
                <td>{{$item->message}}</td>
            </tr>
        @endforeach
    </table>
@endsection

@section('footer')
    cpoyright 2020 tyyano.
@endsection



<!-- <html>
<head>
<title>Hello/Index</title>
<style>
body {font-size:16pt; color:#999;}
h1 { font-size:100pt; text-align:right; color:#eee;
    margin:40px 0px -50px 0px; }
</style>
</head>
<body>
    <h1>Blade/Index</h1>
    @isset ($msg)
    <p>こんにちは、{{$msg}}さん。</p>
    @else
    <p>何か書いて下さい</p>
    @endisset
    <form method="POST" action="/hello">
        @csrf
        <input type="text" name="msg">
        <input type="submit">
</from>
    <p>This is a sample page with php-template.</p>
</body>
</html> -->
