@extends('layouts.helloapp')

@section('title', 'Add')

@section('menubar')
    @parent
    新規作成ページ
@endsection

@section('content')
<table>
        <form action="add" method="post" enctype="multipart/form-data">
            {{csrf_field()}}
            <tr>
                <th>title:</th>
                <td><input type="text" name="title"></td>
            </tr>
            <tr>
                <th>message:</th>
                <td><textarea type="text" name="message"></textarea></td>
            </tr>
            <tr>
                <th>image:</th>
                <td><input type="file" name="image"></td>
            </tr>
            <tr>
                <th></th>
                <td><input type="submit" value="send"></td>
            </tr>
        </form>
    </table>
@endsection

@section('footer')
cpoyright 2020 Transla
@endsection
