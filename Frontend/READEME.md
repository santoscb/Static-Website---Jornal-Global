## Criação do bucket S3

Para que p website pudesse ser acessado pelo público foi criado um bucket S3 com o nome `jornalglobal`, onde os arquivos index.html, css.css e js.js foram colocados. Para permitir que o bucket fizesse o host do website foi habilitado `static website hosting`. Na parte de permissões foi garantido o acesso público à URL e criada a seguinte bucket policy:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::jornalglobal/*"
        }
    ]
}
```
