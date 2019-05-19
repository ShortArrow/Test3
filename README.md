# Test3

## Enviroment Cloning

### After pull

After the pull, Please do these tasks.

#### Conda PackageList Clone

`conda env create --file requirements.yml`

#### NPM PackageList Clone

1. タスクの実行
2. npm install (home/static/home)

### Before commit

Before the commit,Please do these tasks.

#### Conda PackageList Save

`conda env export > requirements.yaml`

#### NPM PackageList Save

`npm install xxx`

dont need `--save` option

#### output ERD to PDF

`python manage.py graph_models -a -g -o graph-model.pdf`

### 参考

conda environments cloning
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment
